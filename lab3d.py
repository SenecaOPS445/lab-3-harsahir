#!/usr/bin/env python3

'''Lab 3 script - free disk space'''
# Author ID: 165357187 (hs100)

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}' as a new process
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
