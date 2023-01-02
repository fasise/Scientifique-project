#!/bin/bash

# gather the coverage data
python3 -m pip install codecov
if [[ $MATRIX_DOCKER ]]; then
  python3 -m coverage xml --ignore-errors
else
  python3 -m coverage xml
fi
