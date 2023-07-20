#!/bin/bash

# Author: Marley Mulvin Broome
# Date: 2023-07-20
# Description: Run pytest on all tests in the tests directory with as many CPUs as possible

# check pytest exists
if ! command -v pytest &> /dev/null
then
    echo "pytest could not be found"
    exit 1
fi

# ask for coverage report
read -p "Do you want a coverage report? (y/n) " -n 1 -r

if [[ $REPLY =~ ^[Yy]$ ]]
then
    python -m pytest -n auto --cov=src --cov-report=html --cov-report=term --cov-fail-under=50 -- tests/test_*.py

    xdg-open htmlcov/index.html
    exit 0
fi

python -m pytest -n auto -- tests/test_*.py