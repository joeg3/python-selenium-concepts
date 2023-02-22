# python-selenium-concepts
A repo I created when leaarning Selenium with Python

## Run tests
- `poetry run pytest -vs` runs all tests
- `poetry run pytest -vs --html=./reports/demo-test.html` generates html report
- `poetry run pytest -vs -n 3` runs three tests at a time in parallel

## Run reports

## Libraries used
- `pytest-html` for generating HTML reports
- `pytest-xdist` for parallel execution of tests