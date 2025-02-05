#! /usr/bin/bash

pip install -r requirements.txt
mkdir check-reports
pylint --output-format=text:check-reports/lint-report.txt mathlib/
pytest --cov=mathlib --cov-fail-under=90 --cov-report=term-missing --cov-report=html -v --junit-xml=check-reports/tests-report.xml