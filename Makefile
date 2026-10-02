# Makefile for pediatric-icu-drug-titration-calculator project

.PHONY: test build clean

PYTEST_FLAGS = --verbose

all: test

# Run tests

.PHONY: test

test:
	@echo "Running tests..."
	@python -m pytest $(PYTEST_FLAGS) -v tests/

# Build the project (optional, for packaging)

.PHONY: build

build:
	@echo "Building the project..."
	@poetry build

# Clean up build artifacts

.PHONY: clean

clean:
	@echo "Cleaning up..."
	@poetry run rm -rf dist build *.egg-info