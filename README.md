# AirJnR Console

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210523T183726Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f9dbfc52232268633f8b4f7cc510bb8b3dfde1569c6f4c52495f8a86af9720a9)

## Description

The console is the backend section of a project to recreate the AirBnB website.

The console is a command line interpreter that allows for management of data. From the console, a user can create, modify, and delete objects without a visual interface for development and debugging purposes.

An archive of available data is saved in a JSON file that is transportable across different programs. This storage file contains information about each particular object and can be updated to reflect changes. When the program exits, the stored information is still available and can be reloaded upon the next entry into the program.

By default, each object is prepopulated with a unique identification number so the particular instance can be specified, as well as the original time of creation and the last time changes were made. Some other suggested information is available by default but not autopopulated, and any other information can be added at the user's discretion.

Some features for full usage are not available as of yet, but the functionality has been created.

## Installation

To install, clone this repository into your system with the command:

```
$ git clone https://github.com/RLewis11769/AirBnB_clone
```

## Usage

The console is now ready for use in either interactive or non-interactive mode.
### Interactive Mode

In interactive mode, the user can have ongoing interaction with the program. A prompt will be provided that will remain until the user exits from this mode. To learn more about using the console, enter the "help" command.

To enter interactive mode, enter "./console.py".

```
$ ./console.py
(hbtn) [desired command]
(hbtn) [output]
(hbtn) quit
$
```

### Non-Interactive Mode

In non-interactive mode, the user can have a one-time interaction with the program.

To use the program in non-interactive mode, echo a command in quotes and "pipe" it into the program as seen below.

```
$ echo "[desired command]" | ./console
$ [output]
$
```

## Features

For basic information and navigation of the console:

| Command | Usage | Description |
|:-------:|:-----:|-------------|
| help | help or help [command] | On its own, displays a list of available commands. With a command, provides a short description of the command. |
| quit| quit | Exits interactive mode. |
| EOF | ctrl-d | Indicates end of file. Exits interactive mode. |

The program uses several commands that assist in creating, modifying, and deleting information at object level as well as in the JSON file:

| Command | Usage | Description |
|:-------:|:-----:|-------------|
| create | create [class] | Creates a new instance of specified class. Prints id of new instance. |
| all | all or all [class] | On its own, prints all instances of any object. If class name is specified, prints all instances of specified class. |
| show | show [class] [id] | Prints all existing information about specified instance. |
| destroy | destroy [class] [id] | Deletes specified instance. Nothing is printed if successful. |
| update | update [class] [id] [attribute] "[information]" | Updates specified instance. If the attribute doesn't exist, it is created. If it does exist, the information is replaced. Nothing is printed if successful. |

Some commands call on the class or instance directly:

| Command | Description |
|:-------:|-------------|
| [class].all() | Prints all instances of specified class. |
| [class].count() | Prints count of all instances of specified class. |
| [class].show("[id]") | Prints all existing information about specified instance. |
| [class].destroy("[id]") | Deletes specified instance. Nothing is printed if successful. |

There are two class-based methods to update information, via a string or dictionary:

| Command | Description |
|:-------:|-------------|
| [class].update("[id]", "[attribute]", [information]) | String method to update specified instance. If the attribute doesn't exist, it is created. If it does exist, the information is replaced. Nothing is printed if successful. |
| [class].update("[id]", [dictionary]) | Dictionary method to update specified instance. Multiple attributes can be updated at once. If an attribute doesn't exist, it is created. If it does exist, the information is replaced. Nothing is printed if successful. |

## Available Classes

- User
- State
- City
- Amenity
- Place
- Review

## Examples

See a list of help topics with:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

Create a user in non-interactive mode with:

```
$ echo "create User" | ./console.py
(hbnb) 466b8dd9-ad30-4ede-be15-d93ced7c5a11
(hbnb)
$
```

Update multiple attributes at a time using the dictionary method at class level with:

```
(hbnb) User.update("466b8dd9-ad30-4ede-be15-d93ced7c5a11", {'first_name': 'Betty', 'last_name':'Holberton'})
(hbnb)
```

Check that the information updated properly:
```
(hbnb) all
["[User] (466b8dd9-ad30-4ede-be15-d93ced7c5a11) {'id': '466b8dd9-ad30-4ede-be15-d93ced7c5a11', 'updated_at': datetime.datetime(2021, 5, 23, 19, 35, 28, 83766), 'last_name': 'Holberton', 'first_name': 'Betty', 'created_at': datetime.datetime(2021, 5, 23, 19, 32, 2, 282053)}"]
(hbnb)
```

## Testing

Unittests are defined for this project to ensure proper implementation. See the [tests](https://github.com/RLewis11769/AirBnB_clone/tree/main/tests) folder for more details.

To test the project, execute the following command:

```
$ python unittest -m discover tests
```

## Bugs

The console assumes arguments are always in the correct order, commands are separated by proper delimeters (spaces or commas and spaces), and quotes are properly used to surround certain arguments as defined under Usage. Improper usage will result in undefined behavior.

## Authors

AirJnR was written by Jacob Chavera and Rachel Lewis. See [AUTHORS](https://github.com/RLewis11769/AirBnB_clone/blob/main/AUTHORS) page for more details.

Due 5/24/2021
