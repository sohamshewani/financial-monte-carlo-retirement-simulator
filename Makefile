all: main

main: requirements.txt
	pip install -r requirements.txt
	python -m venv venv
	. ./venv/bin/activate
	python -m unittest discover -s tests
	python main.py

dist: clean
	python setup.py sdist
	twine upload dist/*

clean:
	rm -rf venv
	rm -rf dist
	rm -rf build
	rm -rf .eggs
	rm -rf .pytest_cache
	rm -rf .cache
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '__pycache__' -exec rm -fr {} \;

test: clean
	python -m unittest discover -s tests
