#!/bin/bash

# ensure you are in the sffloat directory, e.g.: cd ~/workspace/sffloat
rm dist/*
python3 setup.py sdist
python3 -m pip wheel --no-build-isolation --no-deps --wheel-dir dist dist/*.tar.gz
