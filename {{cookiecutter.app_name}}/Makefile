# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS

# Build the container
build: ## Build the container release
	docker compose -f docker-build.yml build

# Build the container
build-nc: ## Build the container without caching
	docker compose build --no-cache

# Build and run the container
up: ## Spin up the project
	docker compose up --build

test: ## Run tests from the project
	docker compose run --rm django python manage.py test

stop: ## Stop running containers
	docker compose stop

down: ## Down running containers
	docker compose down

clean: stop ## Stop and clean running containers
	docker compose down -v

migrate: ## Performs database migrations
	docker compose run --rm django python manage.py migrate

makemigrations: ## Create database migrations
	docker compose run --rm django python manage.py makemigrations

createsuperuser: ## Create admin user
	docker compose run --rm django python manage.py createsuperuser
