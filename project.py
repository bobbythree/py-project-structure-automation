#!/usr/bin/env python3

import os
import sys

def main():
    parent_dir = os.getcwd()    
    project_name = sys.argv[1]
    path = os.path.join(parent_dir, project_name)
    os.mkdir(path)
    # print("dir '%s' created" %project_name)
    

if __name__ == "__main__":
    main()
