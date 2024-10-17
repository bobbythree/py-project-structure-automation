## This Python script automates the setup of a python project's file structure in the current working directory  

The script is initiated by typing ```py-project``` into the terminal followed by the name of your project.  
i.e. the command ```py-project asdf``` will create a folder called 'asdf' in the current directory.  
Inside the root directory is a blank README.md file, .gitignore file, src/ directory and tests/ directory  
Inside the src/ directory is a blank main.py file.  
 

## file structure:  
root/  
--README.md  .gitignore  src/  tests/  

src/  
--main.py  

tests/

  

## to run as a binary on Linux:  
 - clone this repo to local machine  
 - copy py-project.py script to /usr/local/bin  
 - rename script without .py extension with ```mv py-project.py py-project```
 - change permissions for the file with ```chmod +x py-project```
 - change ownership of script with ```chown [your-username]:[group-name] py-project```
 - open terminal in directory of your choice  
 - type ```py-project [name of your project]```  


## to run not as a binary:
 - clone repo to local machine  
 - open terminal in project's root directory  
 - type python ```py-project.py [name of your project]```
