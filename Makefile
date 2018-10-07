install:
	pip install -r requirements.txt

compile_file:
	python cms-static-web-compiler.py $(file_source)