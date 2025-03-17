#!/bin/bash
black --check sffloat || { echo 'black failed (use black first)' ; exit 1; }
python3 -m pylint -r n sffloat || { echo 'pylint failed' ; exit 1; }
python3 -m nose2 || { echo 'automatic test failed' ; exit 1; }