install:
	pip install -r requirements.txt

create_project:
	python3 cms_static_web_compiler.py --name $(project_name)

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info

test: clean
	python3 -m unittest discover -v