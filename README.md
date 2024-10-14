# automated python project file structure

## This program automates the setup of a python project file structure.  

The program is initiated by typing 'py-project' into the terminal followed by the name of your project.  
i.e. the command 'py-project asdf' will create a folder called 'asdf' in the current directory.  
inside the root directory is a blank README.md file, .gitignore file, src/ directory and tests/ directory  
inside the src/ directory is a blank main.py file.  
 

## file structure:  
root/
--README.md .gitignore src/ tests/  

src/  
--main.py  

tests/

  

## to run as a binary on Linux:  
 - clone this repo to local machine  
 - copy project.py file to /usr/local/bin  
 - rename file without .py extension  
 - change permissions for the file with 'chmod +x project'  
 - open terminal in directory of your choice  
 - type project [name of your project]  


## to run not as a binary:
 - clone repo to local machine  
 - open terminal in project's root directory  
 - type python project.py [name of your project]
