.PHONY: install

# Define the install target
install:
	@echo "Installing Python packages..."
	pip install --no-input flask
	pip install --no-input selenium
	pip install --no-input -U pyvo
	@echo "Installation complete."

# Define the clean target (optional)
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	@echo "Cleanup complete."
