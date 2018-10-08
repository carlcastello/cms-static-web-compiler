install:
	pip install -r requirements.txt

create_project:
	python cms_static_web_compiler.py --name $(project_name)