#!/usr/bin/python3
"""
entry point of the command interpreter for AirBnB project
"""
import cmd
import inspect
from models import base_model
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB project
    """
    prompt = "hbnb: "

    def do_prompt(self, line):
        "change the interactive prompt"
        self.prompt = line + ":"

    def emptyline(self):
        """
        Do nothing when no arguement is passed
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        save it to (to the JSON file) and prints
        the id
           Raises:
            If the class name is missing,
            print ** class name missing ** (ex: $ create)
            If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ create MyModel)
        """
        # Check if the argument is empty
        if not arg:
            print("** class name missing **")
            return
        # Check if the argument is a valid class name in my_module
        if not inspect.isclass(getattr(base_model, arg, None)):
            print("** class doesn't exist **")
            return
        # Create a new instance of the class
        obj = getattr(base_model, arg)()
        # Save the instance to the JSON file
        obj.save()
        # Print the id of the instance
        print(obj.id)
    
    def do_show(self, arg):
        """
        Prints the strinf representantion based on the class
        name and id
        Args:
            model: the class name
            id: id of the class
        Raise:
            If the class name is missing,
            print ** class name missing ** (ex: $ show)
            If the class name doesn’t exist, print
             ** class doesn't exist ** (ex: $ show MyModel)
            If the id is missing, print
              ** instance id missing ** (ex: $ show BaseModel)
            If the instance of the class name doesn’t exist for the id,
              print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        # split arg by whitespace
        args = arg.split()
        # check if arguement passed for class and id
        if len(args) == 0:
            print("** class name missing **")
            return
        model = args[0]
        if len(args) == 1:
            print("** instance id missing **")
            return
        id  = args[1]
        # Get id and classname
        
        # Check if the argument is a valid class name in my_module
        if not inspect.isclass(getattr(base_model, model, None)):
            print("** class doesn't exist **")
            return
        # check if the instance of the class name doesnt exist for the id
        # store all instances
        all_objs = storage.all()
        # get instance
        stored_key = str(model) + "." + str(id)
        instance = all_objs.get(stored_key)
        if instance is None:
            # if instance doesnt exist
            print("** no instance foundd **")
        else:
            # print string representation
            print(str(instance))

    def do_quit(self, line):
        """
        The quit exit the program
        """
        raise SystemExit(0)

    def do_EOF(self, line):
        """
        EOF commands that allow the
        user to exit the program by typing quit or pressing Ctrl+D.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
