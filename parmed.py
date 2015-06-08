#!/usr/bin/env python
import os
import sys

# Since this script is called "parmed.py" and we want to import the "parmed"
# package, we need to remove the script's directory from sys.path to prevent the
# script from trying to import itself.
scriptdir = os.path.realpath(os.path.abspath(os.path.split(__file__)[0]))
while True:
    for i, folder in enumerate(sys.path):
        folder = os.path.realpath(os.path.abspath(folder))
        if folder == scriptdir:
            break
    else:
        break
    sys.path.pop(i)

from parmed.scripts import clapp
clapp()
