#!/usr/bin/env python
"""
Care Taker Main Application Suite
Mike Tung
"""

#imports
from apscheduler.schedulers.blocking import BlockingScheduler
import argparse
import os
from services.backup_service import *
from services.tmp_deletion_service import *
import subprocess as sb
import sys

def schedule(func = None):
    """
    Schedules jobs for caretaker to run

    req args:
    func - defaults to None

    returns:
    none
    """

    if func is not None:
        scheduler = BlockingScheduler()
        scheduler.add_job(
                                        func, 
                                        'cron', 
                                        day_of_week=0, 
                                        hour=12,
                                        replace_existing = True)
        print('Current jobs...')
        scheduler.print_jobs()
        print('Starting up job!')
        scheduler.start()
        print('Done!')
    else:
        print('No jobs scheduled')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
                                        '-d', '--delete', 
                                        action='store_true',
                                        default = False,
                                        help = 'initiate delete service')
    parser.add_argument(
                                        '-b', '--backup', 
                                        action='store_true',
                                        default = False,
                                        help = 'initiate backup service')
    parser.add_argument(
                                        '-s', '--schedule',
                                        action='store_true',
                                        default = False,
                                        help = 'initiate scheduler service')
    args = parser.parse_args()

    if args.schedule:
        if args.backup:
            print('Caretaker Backup Service Scheduled!')
            schedule(backup)
        elif args.delete:
            print("Caretaker Deletion Service Scheduled!")
            schedule(delete_tmp)
        elif args.backup and args.delete:
            print("Caretaker Backup and Deletion Service Scheduled!")
            schedule(backup)
            schedule(delete_tmp)

    if args.backup:
        print('Caretaker Backup Service Initiated!')
        backup()
    if args.delete:
        print("Caretaker Deletion Service Initiated!")
        delete_tmp()







