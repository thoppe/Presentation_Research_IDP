import glob, json, collections, sys
import numpy as np
import itertools
from Bio.PDB.Polypeptide import three_to_one
import Bio.SeqUtils.ProtParam as bioseq
import pandas as pd
import multiprocessing as mp

min_bind_energy = -1.5
min_d2o_energy  = -1.5

__mp_CORES = 30

#samples = 100
#binding_targets = 1000

#aa_index = ("ALA CYS ASP GLU PHE GLY HIS ILE LYS LEU MET "
#            "ASN PRO GLN ARG SER THR VAL TRP TYR").split()
#aa_index = [three_to_one(a) for a in aa_index]

# Load the model
f_model_json = "model_system.json"
with open(f_model_json) as FIN:
    js = json.load(FIN)

aa_index = js["interaction_matrix_labels"]
aa_index = [three_to_one(a) for a in aa_index]

# Load the propensities
f_propensities = js["f_propensities"]
with open(f_propensities) as FIN:
    propensities = json.load(FIN)["propensities"]

propensities["IDP"]  = [propensities["IDP"][aa] for aa in aa_index]
propensities["PDB"]  = [propensities["PDB"][aa] for aa in aa_index]
propensities["sIDP"] = [propensities["sIDP"][aa] for aa in aa_index]
for key in propensities:
    propensities[key] = np.array(propensities[key])
    propensities[key] /= propensities[key].sum()

# Doesn't have to be MJ, just a useful variable name
MJ = np.array(js["interaction_matrix"])

MJ_weight_adjustment = 1.5
MJ_weight = np.exp(-js["beta"]*MJ)
MJ_weight *= MJ_weight_adjustment


def compute_counts(seq):
    counts = np.bincount(seq,minlength=20)
    return pd.Series(counts,index=aa_index,dtype=float)

def compute_mol_frac(seq):
    chi  = compute_counts(seq)
    chi /= len(seq)
    return chi 

def count_matrix(input_seq):
    MOLE_FRAC = compute_mol_frac(input_seq)
    n_seq = np.outer(MOLE_FRAC, MOLE_FRAC)
    return n_seq*len(input_seq)

def protein_self_energy(seq):
    n0 = count_matrix(seq)
    E_AVG = MJ*MJ_weight*n0
    return E_AVG.sum()

def contact_energy(seq, surf):

    unified_seq = np.ravel(list(seq)+list(surf))
    n0 = count_matrix(unified_seq)
    OBS_system = MJ_weight*n0

    # Determine the representative fractions

    count_data = {"peptide":compute_counts(seq),
                  "surface":compute_counts(surf)}

    def pair_itr():
        ITR = itertools.combinations_with_replacement(count_data.keys(),r=2)
        for item in ITR: yield item

    weights = {}
    for k1,k2 in pair_itr():
        weights[(k1,k2)] = np.outer(count_data[k1], count_data[k2])

    W_TOTAL  = sum([w for w in weights.values()])
    zero_idx = W_TOTAL==0

    for key_pair in pair_itr():
        weights[key_pair] /= W_TOTAL
        weights[key_pair][zero_idx] = 0

    PAIR_ENERGY = {}
    for k in pair_itr():
        PAIR_ENERGY[k] = (MJ*OBS_system*weights[k]).sum()
    
    return PAIR_ENERGY

__stock_alphabet_index = range(20)
def IDP_random_sequence(size):
    return np.random.choice(__stock_alphabet_index, 
                            size=size, replace=True,
                            p = propensities["IDP"])

def sIDP_random_sequence(size):
    return np.random.choice(__stock_alphabet_index, 
                            size=size, replace=True,
                            p = propensities["sIDP"])

def PDB_random_sequence(size):
    return np.random.choice(__stock_alphabet_index, 
                            size=size, replace=True,
                            p = propensities["PDB"])


def sample_seq((seq, SURFACE_SEQS)):

    U = collections.defaultdict(list)
    data = {}

    data["seq"] = tuple(seq.tolist())

    data["affinity"] = None
    data["average_number_of_binds"] = None
    data["self_energy"] = None
    data["z_score"] = None

    binding_targets = len(SURFACE_SEQS)

    for surf in SURFACE_SEQS:

        for key,value in contact_energy(seq,surf).items():
            U[key].append(value)

    for key in U:
        U[key] = np.array(U[key])

    binding_key = "peptide","surface"

    # Only consider the binding protein -> surface   
    bind_idx = U[binding_key] < min_bind_energy

    for key in U:
        U[key] = U[key][bind_idx]

    zX = U[binding_key]

    if zX.shape[0] < 5: 
        return data

    print "SHAPE", zX.shape

    #time_bound = np.exp(-U[binding_key])
    #time_bound /= time_bound.sum()
    #zX = time_bound

    bottom_percentile_value  = 5
    bottom_percentile  = np.percentile(zX, bottom_percentile_value)
    bottom_percentile_idx = zX <= bottom_percentile
    top_percentile_idx = ~bottom_percentile_idx

    z_score  = zX[top_percentile_idx].mean()
    z_score -= zX[bottom_percentile_idx].mean()
    z_score /= zX[top_percentile_idx].std()

    data["z_score"] = z_score

    U_TOTAL = sum(U.values())
    u_self  = protein_self_energy(seq)

    data["affinity"] = np.average(U[binding_key])
    data["average_number_of_binds"] = sum(bind_idx)/float(binding_targets)
    data["self_energy"] = u_self
    print data
    return data
    exit()

    change_self_energy_binding = (U[('peptide','peptide')] 
                                  - u_self)

    # disorder_to_order => d2o
    d2o_idx = change_self_energy_binding < min_d2o_energy
    data["d2o_averaged_mol_surface"] = compute_mol_frac([])
    data["d2o_averaged_mol_surface"][:] = 0

    if d2o_idx.any():
        data["d2o_energy_change"] = change_self_energy_binding[d2o_idx].mean()
        data["d2o_average_number_of_binds"] = sum(d2o_idx)/float(binding_targets)        

        for idx in np.where(d2o_idx)[0]:
            data["d2o_averaged_mol_surface"] += compute_mol_frac(SURFACE_SEQS[idx])

        #print data["d2o_averaged_mol_surface"]
        data["d2o_averaged_mol_surface"] /= d2o_idx.sum()

    else:
        data["d2o_energy_change"] = np.nan
        data["d2o_average_number_of_binds"] = 0

    data["d2o_averaged_mol_surface"] = data["d2o_averaged_mol_surface"].tolist()
        

    return data


def sample_system(PEPTIDE_SEQS, SURFACE_SEQS, parallel=False):  
    
    if parallel: 
        P = mp.Pool(__mp_CORES)

    data = collections.defaultdict(list)

    input_iter = ((seq, SURFACE_SEQS) for seq in PEPTIDE_SEQS)

    if parallel:
        ITR = P.imap(sample_seq, input_iter)
    else:
        ITR = itertools.imap(sample_seq, input_iter)

    for i, item_data in enumerate(ITR):
        print "HERE", i, item_data
        for key in item_data:
            data[key].append(item_data[key])

    if parallel:
        P.close()
        P.join()

    return data

