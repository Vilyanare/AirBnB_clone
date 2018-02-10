#!/usr/bin/python3
"""Module containing entrypoint to command interpreter for AirBnB_clone project"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB_clone project

    Attributes
    prompt - what to display for command line prompt
    chk_class - Tuple with classes that can be created
    """
    prompt = "(hbnb)"
    chk_class = ("BaseModel", "User")

    def do_create(self, arg):
        """Create a new instace of provided class"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.chk_class:
            print("** class doesn't exist **")
        else:
            b = eval("{}()".format(arg))
            b.save()
            print(b.id)

    def do_show(self, arg):
        """Print string representation of an instance based on provided class and ID"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in self.chk_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage._FileStorage__objects:
            print("** no instance found **")
        else:
            eval("print({}(**storage._FileStorage__objects['{}.{}']))".format(args[0], args[0], args[1]))

    def do_destroy(self, arg):
        """Delete an instance based on provided class and ID"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in self.chk_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage._FileStorage__objects:
            print("** no instance found **")
        else:
            del storage._FileStorage__objects['{}.{}'.format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints string representations of all instances of provided class"""
        if arg not in self.chk_class:
            print("** class doesn't exist **")
        else:
            for k in storage._FileStorage__objects:
                if arg in k:
                    eval("print({}(**storage._FileStorage__objects['{}']))".format(arg, k))

    def do_update(self, arg):
        """Updates an instance of provided class and ID with key/value pair"""
        args = arg.split()
        if arg == "":
            print("** class name is missing **")
        elif args[0] not in self.chk_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage._FileStorage__objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            storage._FileStorage__objects['{}.{}'.format(args[0], args[1])]['{}'.format(args[2])] = args[3]
            storage.save()


    def emptyline(self):
        """Overwriting default action of emptyline to do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_EOF(self, arg):
        """If EOF then exit the interpreter"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
