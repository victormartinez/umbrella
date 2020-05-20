clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

check:
	black --target-version py37 tests --check
	black --target-version py37 umbrella --check
	flake8 --max-line-length=88 umbrella
	flake8 --max-line-length=88 tests

black:
	black --target-version py37 umbrella
	black --target-version py37 tests

test:
	OPEN_WEATHER_API_KEY="" pytest -v
