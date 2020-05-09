install_requirements:
	pip install -r requirements.txt

install_requirements_build:
	pip install -r requirements_build.txt

start_app:
	docker-compose up

connect_to_database:
	docker exec -it database psql lol-stats user

format:
	yapf -i -r sources/ --style='{based_on_style: pep8, indent_width: 4}'
