#! /usr/bin/bash

# install requirements
pip install --upgrade pip
pip install -r requirements.txt

# cleanup
rm -rf check-reports
mkdir check-reports

# run linter
pylint --output-format=text:check-reports/lint-report.txt mathlib/

# run tests with coverage report and junit report
pytest --cov=mathlib --cov-fail-under=90 --cov-report=term-missing --cov-report=html -v --junit-xml=check-reports/tests-report.xml