build:
	docker-compose -f docker-compose.yaml build

up:
	docker-compose -f docker-compose.yaml up --force-recreate

down:
	docker-compose -f docker-compose.yaml down 

volumes-prune:
	docker-compose -f docker-compose.yaml down --volumes

migrate:
	docker-compose -f docker-compose.yaml run --rm --entrypoint="" web python manage.py migrate

migrations:
	docker-compose -f docker-compose.yaml run --rm --entrypoint="" web python manage.py makemigrations

run:
	docker-compose -f docker-compose.yaml run --rm --entrypoint="" --service-ports web python manage.py $(cmd) 

migrate:
	docker-compose -f docker-compose.yaml run --rm --entrypoint="" web python manage.py migrate

shell:
	docker-compose -f docker-compose.yaml run --rm --entrypoint="" web python manage.py shell

bash:
	docker-compose -f docker-compose.yaml run --rm --entrypoint="" web bash
