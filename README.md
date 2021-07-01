<p align="center"><img src="https://camo.githubusercontent.com/7e9956678cbe5ec1d712dde039115910e2002db17bc7ff7e7d1638915c500827/68747470733a2f2f692e6962622e636f2f324e42596259762f434c4f4e312e706e67" width="676" height="285"/></p>

# AirBnB clone - The console

In this project of Airbnb_clone seeks as a first instance to create a console that will cover fundamental concepts of programming in Python such as handling classes, objects, handling JSON files. The objective of the project is to deploy a console with its own commands where eventually you can deploy a web server that will be a copy of the Airbnb website this as a segment project for Holberton School


# Console
The console AirBnB Clone is a line interpreter that allows the user, interact directly from a database <file.json>, editing, creating and removing objects, attributtes and values from the own object

Usage This console can be run both interactively and non-interactively. For a better image of how to do this, here is a example of both methods

** Non-interactive mode **
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
** Interactive mode **
```
./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)help quit
Quit command to exit the program

(hbnb)quit
```

# Console commands

The principle execution file has already all permission needed, with a simple execution in linux environment "./", the console will start
```
ubuntu:~/AirBnB$ ./console.py
```

** create **
Creates a new base BaseModel, or any kind of his instances: City, Amenity, Place, Review, State, User And prints on screen his unique id (uuid4) for a future reffer ; and at the same time, creates a file <file.json> where we could store, manage and save all instances created in the process. ie: "$ create BaseModel"
```
(hbnb)create BaseModel
a3e2850a-41c9-490b-8c26-af9f65d64fff
```

** show **
Prints the string representation of an instance based on the class name and id "$ show BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff"
```
(hbnb)show BaseModel a3e2850a-41c9-490b-8c26-af9f65d64fff
[BaseModel] (a3e2850a-41c9-490b-8c26-af9f65d64fff) {'id': 'a3e2850a-41c9-490b-8c26-af9f65d64fff', 'created_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959773), 'updated_at': datetime.datetime(2021, 7, 1, 6, 57, 25, 959998)}
```
## Functions
| Funcion | Description |
|---------|-------------|
| main.c  | contains the call to system functions |
| op_functions1.c | contains the call to the function push, pall, pint and pop |
| op_functions2.c | contains the call to the function swap, add, nop, sub and div |
| op_rotr.c | rotates the stack to the bottom |
| processing_file_name.c | contains the buffer_clean and processes each line of the file introduced. |
| selector.c |  selects function of opcode related to the line of monty |
|stack_operations.c | determines the length of a stack |
| strings.c| Determines the strings length. |

## Authors ✒️
- **Adriana Echeverri** - [adri-er](https://github.com/adri-er)
- **Juan Sebastian Tovar** - [juanstm200](https://github.com/juanstm200)
