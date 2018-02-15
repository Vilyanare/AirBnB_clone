#!/usr/bin/python3
"""Module containing entrypoint to command interpreter
for AirBnB_clone project"""
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB_clone project

    Attributes
    prompt - what to display for command line prompt
    objdict -
    """
    prompt = "(hbnb) "
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
        """Print string representation of an
        instance based on provided class and ID"""
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
        objlist = []
        if models.classes.get(arg) is None and arg != "":
            print("** class doesn't exist **")
        else:
            for k, v in self.objdict.items():
                if arg == "":
                    objlist.append(v)
                elif arg in k:
                    objlist.append(v)
            print(objlist)

    def do_update(self, arg):
        """Updates an instance of provided class and ID with key/value pair"""
        args = shlex.split(arg)
        if arg == "":
            print("** class name missing **")
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
            obj = self.objdict['{}.{}'.format(args[0], args[1])]
            if getattr(obj, args[2], None) is not None:
                setattr(obj, args[2], type(
                    getattr(obj, args[2], None))(args[3]))
            else:
                setattr(obj, args[2], args[3])
            models.storage.save()

    def do_count(self):
        """Show number of instances of a class"""

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

    def default(self, arg):
        """Default action if no do command found"""
        args = arg.split('.')
        if args[0] in models.classes:
            if args[1]:
                if args[1].split('()')[0] in self.methods:
                    self.methods[args[1].split('()')[0]](self, args[0])

    methods = {'create': do_create, 'show': do_show,
    'all': do_all, 'count': do_count, 'destroy': do_destroy,
    'update': do_update}

if __name__ == '__main__':
    HBNBCommand().cmdloop()
