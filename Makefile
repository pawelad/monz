# Source: http://clarkgrubb.com/makefile-style-guide
MAKEFLAGS += --warn-undefined-variables
.DEFAULT_GOAL := help

.PHONY: install
install: ## Install package in editable mode
	python -m pip install --upgrade pip wheel
	python -m pip install --editable ".[dev]"

.PHONY: format
format: ## Format code
	black src/ tests/ noxfile.py
	isort src/ tests/ noxfile.py
	ruff --fix src/ tests/ noxfile.py

.PHONY: test
test: ## Run the test suite
	nox

.PHONY: build
build: ## Build package
	python -m flit build

.PHONY: publish
publish: ## Publish package
	python -m flit publish

.PHONY: clean
clean: ## Clean dev artifacts
	rm -rf .coverage coverage.xml .nox/ .pytest_cache/ dist/

# Source: https://www.client9.com/self-documenting-makefiles/
.PHONY: help
help: ## Show help message
	@awk -F ':|##' '/^[^\t].+?:.*?##/ {\
	printf "\033[36m%-40s\033[0m %s\n", $$1, $$NF \
	}' $(MAKEFILE_LIST)
