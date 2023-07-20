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

python -m pytest -n auto -- tests/test_*.py