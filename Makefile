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

# https://www.viget.com/articles/two-ways-to-share-git-hooks-with-your-team/
# If git version >= 2.9
# init:
	# git config core.hooksPath .githooks

# If git version < 2.9
init:
	find .git/hooks -type l -exec rm {} \;
	find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;


# Local execution
create_project:
	python3 cms_static_web_compiler.py --name $(project_name)
