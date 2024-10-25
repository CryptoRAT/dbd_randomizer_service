# Variables
PYTHON = python
PIP = pip
REQUIREMENTS_FILE = requirements.txt
VENV_DIR = venv
ACTIVATE_SCRIPT = $(VENV_DIR)/bin/activate

# Directories to clean
CLEAN_DIRS = build dist *.egg-info .pytest_cache __pycache__

# Task to clean build/dist/library artifacts
clean:
	@echo "Cleaning build and dist directories..."
	rm -rf $(CLEAN_DIRS)
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '*~' -delete

# Task to set up the virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)

activate:
	@if [ ! -f $(ACTIVATE_SCRIPT) ]; then \
		echo "Virtual environment not found! Please run 'make venv' first."; \
		exit 1; \
	fi
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Activating virtual environment..."; \
		. $(ACTIVATE_SCRIPT); \
	else \
		echo "Virtual environment already activated"; \
	fi

# Task to install dependencies in the virtual environment
install: venv
	@if [ ! -f $(ACTIVATE_SCRIPT) ]; then \
		echo "Virtual environment not found! Please run 'make venv' first."; \
		exit 1; \
	fi
	@echo "Activating virtual environment and installing dependencies..."
	. $(ACTIVATE_SCRIPT) && $(PIP) install -r $(REQUIREMENTS_FILE)