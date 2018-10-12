clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info

pyre:
	pyre --show-error-traces check || true

pylint:
	pylint cms_static_web_compiler.py app/	test/

compile: clean pyre pylint

test: clean
	python3 -m unittest discover -v

install:
	pip install -r requirements.txt

build: install compile test

create_project:
	python3 cms_static_web_compiler.py --name $(project_name)

