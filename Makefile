install:
	pip install -r requirements.txt

create_project:
	python3 cms_static_web_compiler.py --name $(project_name)

test_all:
	python3 -m unittest discover -v