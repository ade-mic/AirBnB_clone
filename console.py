#!/usr/bin/python3
"""
entry point of the command interpreter for AirBnB project
"""
import cmd
import inspect
from models import base_model

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
        # members = inspect.getmembers(models)
        if not inspect.isclass(getattr(base_model, arg, None)):
            print("** class doesn't exist **")
            return
        
        # Create a new instance of the class
        obj = getattr(base_model, arg)()
        # Save the instance to the JSON file
        obj.save()
        # Print the id of the instance
        print(obj.id)

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
