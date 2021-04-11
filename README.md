<p align="center"><img src="https://lh5.googleusercontent.com/aqCkUhF3qL-jUfv2h6HCn9pnRehJGs6daseAdHzF7WCQ7s5g1mK0C1rRWX4MOmKlif7vl9FsHXo12w=w1317-h666" class="ndfHFb-c4YZDc-HiaYvf-RJLb9c" alt="Mostrando shell_3.JPG" aria-hidden="true"></P>

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
                     and get the command line
- **select_built_in** : This function validates whether the input argument is a
                        valid command within the system
- **search_dir_com** : This file has the function that validates the input
                       argument and looks in the PATH if the input command exists in the directory
- **exec_com_args** : This file has the function of creating the child process
                      and executing the input argument
## Requirements 🛠️
- Ubuntu 14.04 LTS
- Functions and files will be compiled with gcc 4.8.4 with flags

## Authors ✒️
- **Cristian Pinzón Capera** - [faykris](https://github.com/faykris)
- **Julio Cesar Arenas** - [jihuder](https://github.com/jihuder)
- **Juan Sebastián Tovar** - [juanstm200](https://github.com/juanstm200)
