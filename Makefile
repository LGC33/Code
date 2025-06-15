# Define variables
VENV_NAME?=.venv
PYTHON_VERSION?=3.11
FLASK_VERSION?=2.3.1
SRC=sammelrepository

# Create a virtual environment
venv-create:
	python$(PYTHON_VERSION) -m venv $(VENV_NAME)
	pip install poetry
	poetry install

# Active virtual environment
venv-activate:
	. $(VENV_NAME)/bin/activate

# Remove the virtual environment
venv-clean:
	rm -rf $(VENV_NAME)

source:
	. $(PWD)/.env.sh

# Reset the database migrations and import data from the `Landesrepositories`.
generate-tokens:
	. $(PWD)/.env.sh && \
	python -m sammelrepository generate-tokens

# Reset the database migrations and import data from the `Landesrepositories`.
reset-db:
	. $(PWD)/.env.sh && \
	python -m sammelrepository resetdb

# Run the app in local environment
run-local:
	. $(PWD)/.env.sh && \
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
	. $(PWD)/.env.sh && \
	poetry run pytest
