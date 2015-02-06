title1  = "Multiscale protein modeling Disorder & aggregation"
title2  = "Mean-field lattice-model IDP"
author = "Travis Hoppe"
target1 = "CSULA_2015_talk.md"
target2 = "biophysical_2015_conf.md"

target = $(target2)
title  = $(title2)

python_exec    = python
md2reveal_exec = md2reveal/md2reveal.py

args = --html_title $(title) --html_author $(author) 

all:
	make biophys

CSULA:
	$(python_exec) $(md2reveal_exec) $(target1) --output index.html $(args)

biophys:
	$(python_exec) $(md2reveal_exec) $(target2) --output biophys_index.html $(args)

edit:
	emacs $(target) &

commit:
	@-make push

check:
	find . -maxdepth 1 -name "*.md" -exec aspell check {} \;

view:
	chromium-browser biophys_index.html

clean:
	rm -rvf index.html
	rm -rvf .render_cache/

push:
	git status
	git add index.html Makefile
	git add $(target)
	git add *.md
	git commit -a
	git push

pull:
	git pull

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
# Build dependencies
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

build_deps:
	-git submodule add https://github.com/hakimel/reveal.js.git reveal.js
	-git submodule add https://github.com/thoppe/md2reveal.git md2reveal

	git submodule update --init
	cd reveal.js && git checkout v0.3-1438-g9a89e39 && cd ..
	cd md2reveal && git pull origin master && cd ..
	git submodule status
