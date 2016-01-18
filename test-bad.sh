#!/usr/bin/env bash
python -m virtualenv foo --python python3.5
. ./foo/bin/activate
python -m venv bar
. ./bar/bin/activate
pip install Flask==0.10.1
