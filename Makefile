PROJECT = cms-static-wev-compiler

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info

pylint:
	pylint cms_static_web_compiler.py app/	test/

unittest:
	python3 -m unittest discover -v

install:
	pip install -r requirements.txt

post_pull: install compile run_test

pre_commit:	clean pylint

pre_push: unittest


init:
	git config core.hooksPath .githooks

# Local execution
create_project:
	python3 cms_static_web_compiler.py --name $(project_name)
