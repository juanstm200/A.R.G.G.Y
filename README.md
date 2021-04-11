<p align="center"><img src="https://lh4.googleusercontent.com/GIw7XxPsnDWupIEJ8CJY5AQAQv2QPyAX22CDmGAdS82mF53bvDBU5C-IJDut823MCn8ff3c2nT3HaQ=w763-h666"/></P>

# Simple Shell


This repository contains the program written in C to simulate a Shell, is a command
interpreter where the user has an interface available through which they have the
possibility of accessing the services of the operating system, as well as invocation
or execution of programs

## Files
- **README.md** : Contains the description of how the code works and
                  the description of the files used
- **holberton.h** : Is our header file that contains all the function calls and
                    libraries that will be used in the Shell project
- **get_path_dir** : This file contains the structure to make the call to
                     the PATH and separate it by sud directories
- **get_line_com** : This program contains the function to type at the  prompt
                     and get the command line select_built_in: This function
		     validates whether the input argument is a valid command within the system
- **search_dir_com** : This file has the function that validates the input
                       argument and looks in the PATH if the input command exists in the directory
- **exec_com_args** : This file has the function of creating the child process
                      and executing the input argument
