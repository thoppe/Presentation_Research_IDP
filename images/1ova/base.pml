bg_color white

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
util.chainbow("name CA")
set ray_trace_mode, 4
ray 800, 800
png 1ova_cartoon.png
