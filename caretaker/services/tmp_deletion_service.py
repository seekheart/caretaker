#!/usr/bin/env python
"""
Temp Files/Folder Deletion Service
Mike Tung
"""

#imports
import os
import subprocess as sb
import sys
from services.paths import *

def delete_tmp():
    """
    main function

    req args:
    none

    returns:
    none
    """

    temp_dirs = ['tmp', 'scratch', 'temp']

    for d in directories:
        if d in temp_dirs:
            print('changing to directory {}...'.format(d))
            os.chdir('{}/{}'.format(home_dir, d))
            print('deleting tmp files and folders...')
            sb.run('rm -rf *', shell = True)
            print('Done!')
        os.chdir(current_dir)


if __name__ == '__main__':
    delete_tmp()