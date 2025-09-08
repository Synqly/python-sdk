# Synqly Organization Webhook Demo Makefile

# Variables
VENV_NAME := venv
PYTHON := python3
PIP := $(VENV_NAME)/bin/pip
PYTHON_VENV := $(VENV_NAME)/bin/python
REQUIREMENTS := requirements.txt
MAIN_SCRIPT := webhook_example.py

# Default target
.PHONY: help
help:
	@echo "Synqly Organization Webhook Demo"
	@echo "================================"
	@echo ""
	@echo "Available targets:"
	@echo "  venv        Create virtual environment"
	@echo "  install     Install dependencies"
	@echo "  setup       Create venv and install dependencies"
	@echo "  run         Run the webhook demo script"
	@echo "  clean       Remove virtual environment"
	@echo "  help        Show this help message"
	@echo ""
	@echo "Prerequisites:"
	@echo "  - SYNQLY_ORG_TOKEN environment variable set"
	@echo "  - ngrok installed and authenticated (ngrok authtoken <token>)"
	@echo ""
	@echo "Usage:"
	@echo "  make setup    # Initial setup"
	@echo "  make run      # Run the demo"

# Create virtual environment
.PHONY: venv
venv:
	@echo "🐍 Creating virtual environment..."
	@if [ ! -d "$(VENV_NAME)" ]; then \
		$(PYTHON) -m venv $(VENV_NAME); \
		echo "✅ Virtual environment created in $(VENV_NAME)/"; \
	else \
		echo "ℹ️  Virtual environment already exists"; \
	fi

# Install dependencies
.PHONY: install
install: venv
	@echo "📦 Installing dependencies..."
	@if [ -f "$(REQUIREMENTS)" ]; then \
		$(PIP) install -r $(REQUIREMENTS); \
		echo "✅ Dependencies installed"; \
	else \
		echo "❌ $(REQUIREMENTS) not found"; \
		exit 1; \
	fi

# Setup (create venv + install dependencies)
.PHONY: setup
setup: venv install
	@echo ""
	@echo "🎉 Setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "1. Activate the virtual environment:"
	@echo "   source $(VENV_NAME)/bin/activate"
	@echo ""
	@echo "2. Set your Synqly organization token:"
	@echo "   export SYNQLY_ORG_TOKEN='your-token-here'"
	@echo ""
	@echo "3. Make sure ngrok is authenticated:"
	@echo "   ngrok authtoken YOUR_NGROK_AUTH_TOKEN"
	@echo ""
	@echo "4. Run the demo:"
	@echo "   make run"

# Run the webhook demo
.PHONY: run
run: venv
	@echo "🚀 Running Synqly Organization Webhook Demo..."
	@if [ ! -f "$(VENV_NAME)/bin/python" ]; then \
		echo "❌ Virtual environment not found. Run 'make setup' first."; \
		exit 1; \
	fi
	@if [ -z "$$SYNQLY_ORG_TOKEN" ]; then \
		echo "❌ SYNQLY_ORG_TOKEN environment variable not set"; \
		echo "   Run: export SYNQLY_ORG_TOKEN='your-token-here'"; \
		exit 1; \
	fi
	@echo "Using virtual environment: $(VENV_NAME)"
	$(PYTHON_VENV) $(MAIN_SCRIPT)

# Clean up virtual environment
.PHONY: clean
clean:
	@echo "🧹 Cleaning up..."
	@if [ -d "$(VENV_NAME)" ]; then \
		rm -rf $(VENV_NAME); \
		echo "✅ Virtual environment removed"; \
	else \
		echo "ℹ️  No virtual environment to clean"; \
	fi

# Check prerequisites
.PHONY: check
check:
	@echo "🔍 Checking prerequisites..."
	@if ! command -v $(PYTHON) &> /dev/null; then \
		echo "❌ $(PYTHON) not found"; \
		exit 1; \
	else \
		echo "✅ $(PYTHON) found"; \
	fi
	@if ! command -v ngrok &> /dev/null; then \
		echo "⚠️  ngrok not found"; \
		echo "   Install from: https://ngrok.com/download"; \
		echo "   Then run: ngrok authtoken YOUR_TOKEN"; \
	else \
		echo "✅ ngrok found"; \
	fi
	@if [ -z "$$SYNQLY_ORG_TOKEN" ]; then \
		echo "⚠️  SYNQLY_ORG_TOKEN not set"; \
	else \
		echo "✅ SYNQLY_ORG_TOKEN is set"; \
	fi

# Show environment info
.PHONY: info
info:
	@echo "📋 Environment Information"
	@echo "=========================="
	@echo "Python: $(shell which $(PYTHON))"
	@echo "Virtual Environment: $(VENV_NAME)"
	@echo "Requirements File: $(REQUIREMENTS)"
	@echo "Main Script: $(MAIN_SCRIPT)"
	@echo "Working Directory: $(shell pwd)"
	@echo ""
	@echo "Environment Variables:"
	@echo "  SYNQLY_ORG_TOKEN: $(if $(SYNQLY_ORG_TOKEN),✅ Set,❌ Not set)"
	@echo ""
	@echo "Files:"
	@ls -la
