#!/usr/bin/env python3

import os
import sys

def main():
    #create root dir
    root_dir = os.getcwd()
    project_name = sys.argv[1]

    #path variables
    path = os.path.join(root_dir, project_name)
    path2 = f'{path}/src'
    path3 = f'{path}/tests'

    #create src and test dir
    os.makedirs(path2)
    os.makedirs(path3)

    #create blank files inside directories
    with open(os.path.join(path, "README.md"), 'w') as fp:
        pass

    with open(os.path.join(path, ".gitignore"), 'w') as fp:
        pass

    with open(os.path.join(path2, "main.py"), 'w') as fp:
        pass


if __name__ == "__main__":
    main()
