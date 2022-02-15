all: lint test test-cov

lint:
	poetry run flake8

test:
	poetry run pytest ./tests

test-cov:
	poetry run pytest --cov=revsplit ./tests