build_frontend:
	@echo "Stopping frontend service"
	docker compose -f ./frontend-service/docker-compose.yml down

	@echo "Building frontend service"
	docker compose -f ./frontend-service/docker-compose.yml up -d --build --force-recreate --remove-orphans

	@echo "Done building frontend service"

build_backend: 
	@echo "Stopping backend services"

	@echo "Starting mysql service"
	docker compose -f ./backend/mysql/docker-compose.yaml up -d

	@echo "Starting Redis service"
	docker compose -f ./backend/Redis/docker-compose.yaml up -d

	@echo "Building api service"
	docker compose -f ./backend/docker-compose.yaml up -d --build --force-recreate --remove-orphans

	@echo "Done building backend services"

build_all: build_frontend build_backend
	@echo "All microservices have been built"

stop_all:
	@echo "Stopping all services"

	@echo "Stopping frontend service"
	docker compose -f ./frontend-service/docker-compose.yml down

	@echo "Stopping mysql service"
	docker compose -f ./backend/mysql/docker-compose.yaml down

	@echo "Stopping Redis service"
	docker compose -f ./backend/Redis/docker-compose.yaml down

	@echo "Stopping Api service"
	docker compose -f ./backend/docker-compose.yaml down

.PHONY: build_frontend build_backend build_all stop_all