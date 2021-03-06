#!/usr/bin/python3
"""
The cmd module is mainly useful for building custom shells
that let a user work with a program interactively.
console.py is the entry point command line interpreter for Airbhb project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    prompt = '(hbnb) '

    air_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

    def do_EOF(self, line):
        """EOF to exit the program """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ method called when an empty line is entered in
        response to the prompt.
        onecmd(str): Interpret the argument as though it had been
                     typed in response to the prompt.
        onecmd help us to implement an empty line + ENTER
        shouldnt execute anything
        """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Args:
            arg(str): given class in the command line interpreter
        If the class name is missing, print ** class name missing **
        If the class name doesnt exist, print ** class doesn't exist **
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        else:
            air_bnb_class = HBNBCommand.air_classes[line]
            instance = air_bnb_class()
            instance.save()
            print(instance.id)
            storage.save()

    def do_show(self, line):
        """
        String representation of a id instance
        """
        tokens = line.split(" ")
        if line is None or line == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key = tokens[0] + "." + tokens[1]
            objs_dict = storage.all()
            if key not in objs_dict:
                print("** no instance found **")
            else:
                print(objs_dict[key])

    def do_destroy(self, line):
        """
        Is a command to destroy a instance
        """
        tokens = line.split(" ")
        if line is None or line == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key = tokens[0] + "." + tokens[1]
            objs_dict = storage.all()
            if key not in objs_dict:
                print("** no instance found **")
            else:
                del objs_dict[key]
                storage.save()

    def do_all(self, arg):
        """
        prints all string representation
        """
        #tokens = arg.split()
        all_objs = storage.all()
        objs_list = []

        if len(arg) == 0:
            for value in all_objs.values():
                objs_list.append(str(value))
        elif arg in HBNBCommand.air_classes:
            for key, value in all_objs.items():
                if arg in key:
                    objs_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return False

        print(objs_list)
        """
        if not arg:
            new_list = [str(value) for key, value in storage.all().items()]
        elif arg not in self.air_classes:
            print("** class doesn't exist **")
            return
        else:
            new_list = [str(value) for key,
                        value in storage.all().items() if arg in key]
            if len(new_list) != 0:
                print(new_list)
        """                
    def do_update(self, line):
        """
        Is a command to update
        """
        tokens = line.split(" ")
        
        if line is None or line == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.air_classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif len(tokens) < 3:
            print("** attribute name missing **")
        elif len(tokens) < 4:
            print("** value missing **")
        else:
            key = tokens[0] + "." + tokens[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj_property = tokens[2]
                obj_value = tokens[3]
                setattr(storage.all()[key], obj_property, obj_value)
                storage.save()

    def do_count(self, args):
        """retrieve the number of instances of a
        class: <class name>.count()."""
        counter = 0
        instances = storage.all()
        for key, obj in instances.items():
            if arg in obj.__str__():
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
