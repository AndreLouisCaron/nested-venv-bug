#!/usr/bin/env bash
python3.5 -m venv foo
. ./foo/bin/activate
python -m venv bar
. ./bar/bin/activate
pip install Flask==0.10.1
