# Makefile for installing a Python project

# Variables
VENV = venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python3
PROJECT_NAME = your_project_name

# Targets
.PHONY: install clean

# emoji lib ❌✅❕▶️⏸✔️

install: $(VENV)
	@echo "▶️ - Creating virtual environment..."
	@echo 
	@python3 -m venv $(VENV)
	@echo 
	@echo "▶️ - Installing dependencies..."
	@echo
	@$(PIP) install -r requirements.txt
	@echo 
	@echo "✅ - Installation complete."

clean:
	@echo "Cleaning up..."
	@rm -rf ./images/*
	@echo "Cleanup complete."

run:
	@echo "Checking requirements..." 
	@echo 
	@$(pyhton) main.py