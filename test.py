#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import subprocess
import sys
subprocess.check_output([
    sys.executable, '-m', 'venv', 'foo',
])
subprocess.check_output([
    './foo/bin/python', '-m', 'venv', 'bar',
])
subprocess.check_output([
    './bar/bin/pip', 'install', 'Flask==0.10.1',
])
