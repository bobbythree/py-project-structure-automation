this program automates the setup of a python project's file structure as follows:

-root  
  -src/  
    -main.py  
  -tests/  

 to run as a binary on Linux:
 - clone this repo to local machine
 - copy project.py file to /usr/local/bin
 - rename file without .py extension
 - change permissions for the file with 'chmod +x project'
 - open terminal in directory of your choice
 - type project [name of your project]

 i.e. the command 'project asdf' will create a root directory called 'asdf' with the src and tests directories inside it.

or not as a binary:
- clone repo to local machine
- open terminal in project's root directory
- type python project.py [name of your project]
