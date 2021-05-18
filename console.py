#!/usr/bin/python3
"""Module for HBNBCommand class"""

import cmd
from models.base_model import BaseModel
import models

classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter subclass with class attribute: prompt
    and public instance methods: EOF and quit"""
    prompt = '(hbnb) '

    def emptyline(self):
        """runs nothing when an empty line is encountered"""
        pass

    def do_EOF(self, arg):
        """exits the program"""
        print()
        return True

    def do_quit(self, arg):
        """exits the prgram"""
        return True

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print('** class name missing **')
            return
        for k, v in classes.items():
            if arg == k:
                tmp = v()
                tmp.save()
                print(tmp.id)
                break
        else:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """prints the string representation of an instance based on class name
        and id"""
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        for k, v in classes.items():
            if args[0] == k:
                break
        else:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key, val in models.storage.all().items():
            if args[0] + '.' + args[1] == key:
                print(val)
                break
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """deletes an instance based on class name and id"""
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        for k, v in classes.items():
            if args[0] == k:
                break
        else:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key, val in models.storage.all().items():
            if args[0] + '.' + args[1] == key:
                del models.storage._FileStorage__objects[key]
                models.storage.save()
                break
        else:
            print('** no instance found **')

    def do_all(self, arg):
        """prints all string representations of given class or all objects if
        none given"""
        if arg:
            for k, v in classes.items():
                if arg == k:
                    break
            else:
                print("** class doesn't exist **")
                return
        l = []
        for key, val in models.storage.all().items():
            if arg:
                if arg == key.split('.')[0]:
                    l.append(str(val))
            else:
                l.append(str(val))
        print(l)

    def do_update(self, arg):
        """updates an instance based on the class name and id by adding or
        updating attribute"""
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        for k, v in classes.items():
            if k == args[0]:
                break
        else:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key, val in models.storage.all().items():
            if args[0] + '.' + args[1] == key:
                break
        else:
            print('** no instance found **')
            return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return
        try:
            atype = type(getattr(val, args[2]))
            setattr(val, args[2], atype(args[3][1:-1]))
        except:
            setattr(val, args[2], args[3][1:-1])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
