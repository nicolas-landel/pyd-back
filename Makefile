up:
	docker compose -f docker-compose.local.yml up

build:
	docker compose -f docker-compose.local.yml build

buildup:
	docker compose -f docker-compose.local.yml up --build

down:
	docker compose -f docker-compose.local.yml down

exec:
	docker compose -f docker-compose.local.yml exec django ./manage.py $(filter-out $@,$(MAKECMDGOALS))