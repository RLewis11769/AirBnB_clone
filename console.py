#!/usr/bin/python3
"""Module for HBNBCommand class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter subclass with class attribute: prompt
    and public instance methods: EOF and quit"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """exits the program"""
        print()
        return True

    def do_quit(self, arg):
        """exits the prgram"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
