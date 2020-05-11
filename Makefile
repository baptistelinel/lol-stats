install_requirements:
	pip install -r requirements.txt

install_requirements_build:
	pip install -r requirements_build.txt

run_main:
	PYTHONPATH=sources python sources/main.py

start_app:
	docker-compose up

connect_to_database:
	docker exec -it database psql lol-stats user

format:
	yapf -i -r sources/ tests/ --style='{based_on_style: pep8, indent_width: 4}'

unit_tests:
	PYTHONPATH=sources pytest tests/unit_tests

component_tests:
	PYTHONPATH=sources pytest tests/component_tests

linter:
	pylint sources/
