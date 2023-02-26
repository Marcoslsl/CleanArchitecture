#! /bin/bash

python3 -m pip install pre-commit pytest-cov black pycodestyle pydocstyle
pre-commit install
