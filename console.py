#!/usr/bin/python3
"""Module containing entrypoint to command interpreter
for AirBnB_clone project"""
import cmd
import models
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB_clone project

    Attributes
    prompt - what to display for command line prompt
    objdict - Dictionary with all object instaces
    methods - dictionary of methods in this class
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
        args = shlex.split(arg)
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
        args = shlex.split(arg)
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
        args = arg.split()
        if len(args) > 0 and models.classes.get(args[0]) is None:
            print("** class doesn't exist **")
        else:
            for k, v in self.objdict.items():
                if arg == "":
                    objlist.append(v)
                elif arg.split()[0] in k:
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

    def count(self, arg):
        """Show number of instances of a class"""
        count = 0
        for k in self.objdict.keys():
            if arg in k:
                count += 1
        print(count)

    def update_dict(self, arg):
        """Updates based on a dict"""
        args = arg.split(' ', 2)
        args_to_dict = json.loads(args[2].replace("'", '"'))
        if self.objdict.get('{}.{}'.format(args[0], args[1][1:-1]), None) is None:
            print("** no instance found **")
        else:
            obj = self.objdict['{}.{}'.format(args[0], args[1][1:-1])]
            for k, v in args_to_dict.items():
                if getattr(obj, k, None) is not None:
                    setattr(obj, k, type(
                        getattr(obj, k, None))(v))
                else:
                    setattr(obj, k, v)
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

    def default(self, arg):
        """Default action if no do command found"""
        args = arg.split('.')
        commands = args[0] + ' '
        if args[0] in models.classes:
            if args[1]:
                for k, v in self.methods.items():
                    if k in args[1]:
                        if k == 'update' and '{' in arg:
                            for i in arg.split('(')[1].split(',', 1):
                                commands += i
                            commands = commands[:-1]
                            self.update_dict(commands)
                            break
                        for i in arg.split('(')[1].split(','):
                            commands += i
                        commands = commands[:-1]
                        commands = commands.strip()
                        v(self, commands)
        else:
            print("*** uknown syntax: {}".format(arg))

    methods = {'show': do_show,
               'all': do_all, 'count': count, 'destroy': do_destroy,
               'update': do_update}

if __name__ == '__main__':
    HBNBCommand().cmdloop()
