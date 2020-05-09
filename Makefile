install_requirements:
	pip install -r requirements.txt

start_app:
	docker-compose up

connect_to_database:
	docker exec -it database psql lol-stats user
