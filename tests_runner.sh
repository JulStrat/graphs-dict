#!/bin/sh
export PYTHONPATH="$PWD"
cd ./tests_out
for f in ../graphtheory/*/tests/test*.py; do python "$f"; done
