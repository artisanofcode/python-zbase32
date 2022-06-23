.DEFAULT_GOAL = help

bootstrap:
	poetry install

#: build the projects output files
build: update
	poetry build

#: run continuous integration tasks
ci:
	poetry run isort --check-only .
	poetry run black --check .
	HYPOTHESIS_PROFILE=slow poetry run pytest -vvv --mypy --pylint --pydocstyle --cov --typeguard-packages=zbase32,tests src tests

clean:`
	rm -rf .mypy_cache/ .pytest_cache/ .coverage dist

#: open a repl console
console:
	poetry run python

docs: update
	exit

#: format all source files
format:
	poetry run shed --refactor --py39-plus src/*.py tests/*.py

#: list avalible make targets
help:
	@grep -B1 -E "^[a-zA-Z0-9_-]+\:([^\=]|$$)" Makefile \
		| grep -v -- -- \
		| sed 'N;s/\n/###/' \
		| sed -n 's/^#: \(.*\)###\(.*\):.*/make \2###    \1/p' \
		| column -t  -s '###' \
		| sort

#: run project server locally
server: update
	exit

#: setup the project after a `git clone`
setup: bootstrap

#: run the projects test suite
test:
	poetry run pytest -vvv --mypy --pylint --pydocstyle --cov --cov-report term-missing --typeguard-packages=zbase32,tests src tests

#: update the project after a `git pull`
update: bootstrap

.PHONY: bootstrap build ci clean console docs format help server setup test update