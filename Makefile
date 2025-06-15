# Define variables
VENV_NAME?=.venv
PYTHON_VERSION?=3.11
FLASK_VERSION?=2.3.1
SRC=sammelrepository
ENV_FILE?=$(PWD)/.env.sh

# Create a virtual environment
venv-create:
	python$(PYTHON_VERSION) -m venv $(VENV_NAME)
	pip install poetry
	poetry install

# Activate virtual environment
venv-activate:
	. $(VENV_NAME)/bin/activate

# Remove the virtual environment
venv-clean:
	rm -rf $(VENV_NAME)

# Source environment variables
source:
	[ -f $(ENV_FILE) ] && . $(ENV_FILE) || true

# Reset the database migrations and import data from the `Landesrepositories`.
generate-tokens:
	[ -f $(ENV_FILE) ] && . $(ENV_FILE) || true; \
	python -m sammelrepository generate-tokens

# Reset the database migrations and import data from the `Landesrepositories`.
reset-db:
	[ -f $(ENV_FILE) ] && . $(ENV_FILE) || true; \
	python -m sammelrepository resetdb

# Run the app in local environment
run-local:
	[ -f $(ENV_FILE) ] && . $(ENV_FILE) || true; \
	uvicorn sammelrepository.main:create_app --factory --reload --log-config=./config/log_conf.yaml

# Clean up all compiled Python files and build artifacts
clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -rf build/ dist/ *.egg-info/

lint:
	poetry run black .

ruff:
	poetry run ruff $(SRC)

pyright:
	poetry run pyright $(SRC)

test:
	[ -f $(ENV_FILE) ] && . $(ENV_FILE) || true; \
	poetry run pytest