#!/usr/bin/env python3

""" A sinple script to move two files into ceph_storage/ directory"""

# standard library imports

import shutil    # shell untililties will be used to move files
import os        # provide access to low level os operations
import path

def main():
#    os.chdir('/home/student/mycode/')
#    shutil.move('raynor.obj', 'ceph_storage/')
#    xname = input('What is the new name for kerrigan.obj? ')
#    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


    path_to_file = '/home/student/mycode/jim.obj'
    path = path(path_to_file)

    if path.is_file():
        print(f'The file {path_to_file} exists')
    else:
        print(f'The file {path_to_file} does not exist')


main()      # this calls our main function
