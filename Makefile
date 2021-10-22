bootstrap:
	poetry install
	poetry run pre-commit install --install-hooks

ci:
	poetry run black --check src tests
	poetry run flake8 --max-line-length 88 --ignore E203
	poetry run mypy src tests
	poetry run pylint src tests
	poetry run pytest -Werror --tb=short --cov=zbase32 --cov-branch --cov-report=term-missing:skip-covered --cov-fail-under=100

console:
	poetry run python

format:
	poetry run shed --py39-plus --refactor src/**/*.py tests/*.py README.md

server: update
	exit
	
setup: bootstrap

test:
	poetry run black --check src tests
	poetry run flake8 --max-line-length 88 --ignore E203
	poetry run mypy src tests
	poetry run pylint src tests
	poetry run pytest -Werror --tb=short --cov=zbase32 --cov-branch --cov-report=term-missing:skip-covered --cov-fail-under=100

update: bootstrap

.PHONY: bootstrap ci console format server setup test update