#! /bin/bash

python3 -m pip install pre-commit pytest black pycodestyle pydocstyle
pre-commit install
