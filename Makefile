package = search_tags_service
tests_dir = tests
test_config = .coveragerc

all: clean test

isort:
	isort -rc $(package)
	isort -rc $(tests_dir)

flake:
	flake8 $(package) $(tests_dir) --max-line-length 120
	@if ! isort -c -rc $(package) $(tests_dir); then \
		echo "Import sort errors, run 'make isort' to fix them!!!"; \
		isort --diff -rc $(package) $(tests_dir); \
		false; \
	fi

test: flake
	pytest -s --quiet --cov-config=$(test_config) \
		--cov=$(package) \
		--cov-report=term \
		--cov-report=html \
		$(tests_dir)

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f `find . -type f -name '*.egg-info' `
	rm -f .coverage
	rm -rf coverage
	rm -rf cover
	rm -rf htmlcov
	rm -rf .cache
	rm -rf .eggs
	rm -rf *.egg-info

.PHONY: all clean flake test test_ci flake_ci