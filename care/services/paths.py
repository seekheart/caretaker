#!/usr/bin/env python
"""
Setup Paths to be used by Services
Mike Tung
"""

import os
import sys

#store directories as variables for use in services
current_dir = os.getcwd()
home_dir = os.path.expanduser('~')
directories = os.listdir(home_dir)

#read in directories from tmp_dirs
tmp_dirs = os.path.join(os.path.dirname(__file__), 'tmp_dirs')

with open(tmp_dirs, 'r') as infile:
    temp_dirs = [line.strip() for line in infile]