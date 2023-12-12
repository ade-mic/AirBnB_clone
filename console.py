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
    prompt = "(hbnb) "

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
            print("** no instance found **")
        else:
            # print string representation
            print(str(instance))

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file).
         Ex: $ destroy BaseModel 1234-1234-1234
        Args:
            model: the class name
            id: id of the class
        Raise:
            If the class name is missing,
            print ** class name missing ** (ex: $ destroy)
            If the class name doesn’t exist, print
             ** class doesn't exist ** (ex: $ destroy MyModel)
            If the id is missing, print
              ** instance id missing ** (ex: $ destroy BaseModel)
            If the instance of the class name doesn’t exist for the id,
              print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        # split arg by whitespace
        args = arg.split()
        # check if arguement passed for class and id
        if len(args) == 0:
            print("** class name missing **")
            return
        # Get id
        model = args[0]
        if len(args) == 1:
            print("** instance id missing **")
            return
        # Get classname
        id  = args[1]     
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
            # delete instance
            del all_objs[stored_key]
            storage.save()
  
    def do_all(self, arg):
        """
        Print all string representation based or not on the
        class name Ex: $ all BaseModel or $ all
        """
        all_objs = storage.all()
        result = []
        if len(arg) == 0:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                result.append(str(obj))
        elif len(arg) > 0:
        # Check if the model is a valid class name in my_module
            if not inspect.isclass(getattr(base_model, arg, None)):
                print("** class doesn't exist **")
                return
            for obj_id in all_objs.keys():
                class_name, id = obj_id.split(".")
                # check if class_name is model
                if class_name == str(arg):
                    obj = all_objs[obj_id]
                    result.append(str(obj))
        print(result)
        return
       

    def do_update(self, arg):
        """
         Updates an instance based on the
         class name and id by adding or updating attribute
         Usage: update <class name> <id> <attribute name> "<attribute value>"
         Raises:
            If the class name is missing,
             print ** class name missing ** (ex: $ update)
            If the class name doesn’t exist,
             print ** class doesn't exist ** (ex: $ update MyModel)
            If the id is missing,
              print ** instance id missing ** (ex: $ update BaseModel)
            If the instance of the class name doesn’t exist for the id,
              print ** no instance found ** (ex: $ update BaseModel 121212)
            If the attribute name is missing,
              print ** attribute name missing ** (ex: $ update BaseModel existing-id)
            If the value for the attribute name doesn’t exist,
              print ** value missing ** (ex: $ update BaseModel existing-id first_name)
            All other arguments should not be used 
            (Ex: $ update BaseModel 1234-1234-1234 email
            "aibnb@mail.com" first_name 
            "Betty" = $ update BaseModel 1234-1234-1234
              email "aibnb@mail.com")
        """
        # split arg by whitespace
        args = arg.split()
        # check if classs name is passed
        if len(arg) == 0:
            print("** class name missing **")
            return
        # check if class name exist
        if not inspect.isclass(getattr(base_model, args[0], None)):
            print("** class doesn't exist **")
            return
        # check if id is missing
        if len(arg) == 1:
            print("** instance id missing **")
            return
        # check if the instance of the class name doesnt exist for the id
        # store all instances
        all_objs = storage.all()
        # get instance
        stored_key = str(args[0]) + "." + str(args[1])
        instance = all_objs.get(stored_key)
        if instance is None:
            # if instance doesnt exist
            print("** no instance found **")
            return
        # check if attribure name is inputted
        if len(args) == 2:
            print("** attribute name missing **")
            return
        # Get attribute name
        attr_name = args[2]
         # Check if attribute name exists
        if len(args) == 3:
            print("** value missing **")
            return
        # setattr(all_objs[stored_key], attr_name, args[3])
        # print(type(args[3]))
        # storage.save()
        # if the attribute name is not one of the "simple" arguments
        # if the attribute name is one of the reserved attributes
        try:
            # cast the attribute value to the attribute type
            attr_value = type(getattr(all_objs[stored_key], attr_name))(args[3])
        except ValueError:
            # if casting fails
            print("** invalid attribute value")
            return
        # update the attribute
        setattr(all_objs[stored_key], attr_name, attr_value)
        # open the JSON file in write mode
        storage.save()
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
