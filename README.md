<p align="center"><img src="https://scontent.fbog9-1.fna.fbcdn.net/v/t1.6435-9/172550315_803847740550102_5114656974240732671_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=730e14&_nc_ohc=kUK7UflG3jcAX8h7E3D&_nc_ht=scontent.fbog9-1.fna&oh=84d5f07e532b6070eead4c134db20862&oe=6097F554"/></p>

# CShell :computer:


The shell is a command that reads lines from a file or terminal, interprets them, and usually executes other commands. This is the program that runs when a user logs on to the system. The shell implements a language that has flow control constructs, a macro installation that provides a variety of features in addition to data storage. It incorporates many features to help interactive use and has the advantage that interpretive language is common to both interactive and non-interactiveuse. That is, commands can be written directly to the running shell or placed in a file and the shell can run the file directly

## Example
This example shows that the **ls -l** command is written at the Shell prompt which
checks whether the command exists and if so the command is interpreted and sends
it to the kernel which executes the command to list all files and
directories and print them on the screen

<p align="center"><img src="https://imgs.developpaper.com/imgs/201810890740605.png"\>


## INTECRACTIVE AND NON-INTERACTIVE SHELL

### Interactive mode:

Commands are executed within the shell execution line, until you are given the output command using Ctrl-D for End of File (EOF) or by using the exit command.

### Non-interactive mode:

Commands are executed externally by sending arguments to the executable of our shell, either a text containing the arguments or content of an archiveor

## Compile
In order to build the project you need to have all the files and put the following command

$ gcc -Wall -Werror -Wextra -pedantic holberton.h *.c -o hsh

which generates an executable called **hsh** with which you can run the simple Shell and test commands 

## Files :open_file_folder:

- **README.md** : Contains the description of how the code works and
                  the description of the files used.
- **holberton.h** : Is our header file that contains all the function calls and
                    libraries that will be used in the Shell project.
- **get_path_dir** : This file contains the structure to make the call to
                     the PATH and separate it by sud directories.
- **get_line_com** : This program contains the function to type at the  prompt
                     and get the command line.
- **select_built_in** : This function validates whether the input argument is a
                        valid command within the system.
- **search_dir_com** : This file has the function that validates the input
                       argument and looks in the PATH if the input command exists in the directory.
- **exec_com_args** : This file has the function of creating the child process
                      and executing the input argument.

## Syscall
| Syscall | Description |
| ------ | ------ |
| Execve | replaces the process that is running with a new process |
| Fork | creates a new process in another memory, the new process is called a son and the old father |
| Wait | the call to the waiting system suspends the execution of the call process |
| Kill | It is a call to the system sends a signal to a process for kill process |
| Exit | Exit causes the normal termination of the process. |


## Requirements 🛠️
- Ubuntu 14.04 LTS
- Functions and files will be compiled with gcc 4.8.4 with flags

## Authors ✒️
- **Cristian Pinzón Capera** - [faykris](https://github.com/faykris)
- **Julio Cesar Arenas** - [jihuder](https://github.com/jihuder)
- **Juan Sebastián Tovar** - [juanstm200](https://github.com/juanstm200)
