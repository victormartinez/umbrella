clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

check:
	black --target-version py37 umbrella --check
	flake8 --max-line-length=88 umbrella

black:
	black --target-version py37 umbrella

test:
	pytest
