# PythonPratice

# Setting up virtual python environment:

Virtual environments enable you to have an isolated space on your computer for Python projects, ensuring that each of your projects can have its own set of dependencies that won’t disrupt any of your other projects.

# Commands

mkdir environments
cd environments

python3 -m venv my_env

ls my_env

Output:
bin include lib lib64 pyvenv.cfg share

# To use the environment, type following

source my_env/bin/activate

it will add prefix as below:

(my_env) J629YF6XTD:environments

# Creating a Simple Program

This prefix lets us know that the environment my_env is currently active, meaning that when we create programs here they will use only this particular environment’s settings and packages.

Note: Within the virtual environment, you can use the command python instead of python3, and pip instead of pip3 if you would prefer. If you use Python 3 on your machine outside of an environment, you will need to use the python3 and pip3 commands exclusively.

Now that we have our virtual environment set up, let’s create a simple “Hello, World!” program. This will make sure that our environment is working and gives us the opportunity to become more familiar with Python if we aren’t already.
To do this, we’ll open up a command-line text editor such as nano and create a new file:
(my_env) sammy@sammy:~/environments\$ nano hello.py
Once the text file opens up in the terminal window we’ll type out our program:
print("Hello, World!")
