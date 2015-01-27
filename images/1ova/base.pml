bg_color white
set ray_opaque_background, off

set antialias, 2
set ray_trace_mode, 4
zoom all, 0, complete=1
show spheres

ray 800, 800
png 1ova_spheres.png

hide spheres
set ray_trace_mode, 0
show lines
ray 800, 800
png 1ova_lines.png

hide lines
show cartoon
set cartoon_fancy_helices=1
set cartoon_flat_sheets = 1.0
set cartoon_smooth_loops = 0

color red, ss h
color marine, ss s
color black, ss l+''
# util.chainbow("name CA")
set ray_trace_mode, 4
ray 800, 800
png 1ova_cartoon.png
