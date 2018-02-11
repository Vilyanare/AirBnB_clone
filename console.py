#!/usr/bin/python3
"""Module containing entrypoint to command interpreter for AirBnB_clone project"""
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB_clone project

    Attributes
    prompt - what to display for command line prompt
    objdict -
    """
    prompt = "(hbnb)"
    objdict = models.storage._FileStorage__objects

    def do_create(self, arg):
        """Create a new instace of provided class"""
        if arg == "":
            print("** class name missing **")
        elif models.classes.get(arg) is None:
            print("** class doesn't exist **")
        else:
            b = models.classes[arg]()
            b.save()
            print(b.id)

    def do_show(self, arg):
        """Print string representation of an instance based on provided class and ID"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif models.classes.get(args[0]) is None:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif self.objdict.get('{}.{}'.format(args[0], args[1])) is None:
            print("** no instance found **")
        else:
            print(self.objdict['{}.{}'.format(args[0], args[1])])

    def do_destroy(self, arg):
        """Delete an instance based on provided class and ID"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif models.classes.get(args[0]) is None:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif self.objdict.get('{}.{}'.format(args[0], args[1])) is None:
            print("** no instance found **")
        else:
            del self.objdict['{}.{}'.format(args[0], args[1])]
            models.storage.save()

    def do_all(self, arg):
        """Prints string representations of all instances of provided class"""
        if models.classes.get(arg) is None and arg != "":
            print("** class doesn't exist **")
        else:
            for k, v in self.objdict.items():
                if arg == "":
                    print(v)
                elif arg in k:
                    print(v)


    def do_update(self, arg):
        """Updates an instance of provided class and ID with key/value pair"""
        args = arg.split()
        if arg == "":
            print("** class name is missing **")
        elif models.classes.get(args[0]) is None:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif self.objdict.get('{}.{}'.format(args[0], args[1])) is None:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            setattr(self.objdict['{}.{}'.format(args[0], args[1])], args[2], args[3])
            models.storage.save()


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
