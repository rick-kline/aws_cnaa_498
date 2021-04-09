install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myreplib tests/*.py
	#python - m pytest --nbval notebook.ipynb

format:
	black *.py

lint:
	pylint --disable=R,C,W main.py

all: install lint format test