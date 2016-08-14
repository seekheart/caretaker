#!/usr/bin/env python
"""
A backup service class 
Mike Tung
"""

#import libs
import os
import subprocess as sb
from services.paths import *
import sys

def update_git_repos(git_dir):
    """
    function to git pull/push repos

    req args:
    git_dir = location of directory as string

    returns:
    none
    """

    git_repos = os.listdir(git_dir)
    message = 'automated update from caretaker'
    for repo in git_repos:
        os.chdir(repo)
        print('Pulling repo {}...'.format(repo))
        sb.run('git pull', shell = True)
        print('Commiting and pushing updates to repo...')
        sb.run('git commit --all -m "{}"'.format(message),
                                shell = True)
        sb.run('git push',
                                shell = True)
        print('Done updating repo {}!'.format(repo))
        os.chdir(git_dir)


def backup():
    """
    master function to run script

    req args:
    none

    returns:
    none
    """
    
    for fi in directories:
        #copy my dot bash files to a backup folder
        if '.bash' in fi:
            print('backing up dotfiles...')
            os.chdir(home_dir)
            print('cp {} ~/dotfiles'.format(fi))
            sb.run('cp {} ~/dotfiles'.format(fi), 
                                                shell= True)
        #backup and update github repos
        elif 'github' in fi:
            os.chdir('{}/{}'.format(home_dir, fi))
            update_git_repos(os.getcwd())

        os.chdir(current_dir)
    


if __name__ == '__main__':
    backup()