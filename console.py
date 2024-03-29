#!/usr/bin/python3
"""
entry point of the command interpreter for AirBnB project
"""
import cmd
import inspect
from models import base_model, user, place, state, city, amenity, review, storage
import shlex

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
        if not any(inspect.isclass(getattr(models, arg, None)) \
        for models in [base_model, user, place, state, city, amenity, review]):
                   print("** class doesn't exist **")
                   return
        # Create a new instance of the class
        if arg == "BaseModel":
            obj = getattr(base_model, arg)()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)
        elif arg == "User":
            obj = getattr(user, arg)()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)
        elif arg == "Place":
            obj = getattr(place, arg)()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)
        elif arg == "State":
            obj = getattr(state, arg)()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)
        elif arg == "City":
            obj = getattr(city, arg)()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)
        elif arg == "Amenity":
            obj = getattr(amenity, arg)()
            # Save the instance to the JSON file
            obj.save()
            # Print the id of the instance
            print(obj.id)
        elif arg == "Review":
            obj = getattr(review, arg)()
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
        if not any(inspect.isclass(getattr(models, model, None)) \
        for models in [base_model, user, place, state, city, amenity, review]):
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
        if not any(inspect.isclass(getattr(models, model, None)) \
        for models in [base_model, user, place, state, city, amenity, review]):
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
        # Check if the model is a valid class name in my_module
        else:
            model = arg
            if any(inspect.isclass(getattr(models, model, None)) \
            for models in [base_model, user, place, state, city, amenity, review]):
                for obj_id in all_objs.keys():
                    class_name, id = obj_id.split(".")
                    # check if class_name is model
                    if class_name == model:
                        obj = all_objs[obj_id]
                        result.append(str(obj))
            else:
                print("** class doesn't exist **")
                return
            
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
        import datetime
        # split arg by whitespace
        args = arg.split()
        # check if classs name is passed
        if len(arg) == 0:
            print("** class name missing **")
            return
        # check if class name exist
        model = args[0]
        if not any(inspect.isclass(getattr(models, model, None)) \
            for models in [base_model, user, place, state, city, amenity, review]):
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
        instance_id = args[1]
        stored_key = "{}.{}".format(model, instance_id)
        instance = all_objs.get(stored_key)
        if instance is None:
            # if instance doesnt exist
            print("** no instance found **")
            return
        # check if attribure name is inputted
        if len(args) == 2:
            print("** attribute name missing **")
            return

         # Check if attribute name exists and not a dictionary
        if len(args) == 3 and not args[2].startswith("{"):
            print("** value missing **")
            return
        # check if the attribute name and value are provided
        if len(args) >= 4 and not args[2].startswith("{"):
            # update with attribute name and value
            attr_name = args[2]
            attr_value = args[3]
            # update the attribute
            setattr(all_objs[stored_key], attr_name, ast.literal_eval(attr_value))
            # update the update_at attribute
            all_objs[stored_key].updated_at = datetime.datetime.now()
            # save it
            storage.save()
        else:
            # update the dictionary representation
            try:
                # Convert string to dictionary
                dict_repr = eval(" ".join(args[2:]))
                self.update_with_dict(all_objs[stored_key], dict_repr)
                # update the update_at attribute
                all_objs[stored_key].updated_at = datetime.datetime.now()
                # save it
                storage.save()
            except Exception as e:
                print(f"Error updating with dictionary representation: {e}")

    def update_with_dict(self, obj, update_dict):
        """
        Update an instance with a dictionary representation
        Args:
            obj: Instance to be updated
            update_dict: Dictionary representation with attributes and values
        """
        for key, value in update_dict.items():
            setattr(obj, key, value)

    def do_count(self, arg):
        """
        Retrieve  the number of instances of a class
        """
        all_objs = storage.all()
        count = 0
        model = arg
        if any(inspect.isclass(getattr(models, model, None)) \
        for models in [base_model, user, place, state, city, amenity, review]):
            for obj_id in all_objs.keys():
                class_name, id = obj_id.split(".")
                # check if class_name is model
                if class_name == model:
                    count += count + 1 
        else:
            print("** class doesn't exist **")
            return
            
        print(count)
        return
            
            

    def default(self, line):
        """
        Handle unrecongnised commands
        """
        # split the line into command and arguements
        args = line.split(".")
        if len(args) == 2:
            command = args[1].strip()
            if command.startswith("show"):
                instance_id = args[1][6:-2]
                instance_id = command[6:-2].strip()
                show_args = f"{args[0]} {instance_id}"
                self.do_show(show_args)
            elif command.startswith("destroy"):
                instance_id = command[9:-2].strip()
                destroy_args = f"{args[0]} {instance_id}"
                self.do_destroy(destroy_args)
            elif command.startswith("update"):
                self.handle_update_command(args[0], command)
            elif command == "all()":
                self.do_all(args[0])
            elif command == "count()":
                self.do_count(args[0])
            else:
                print("*** Unknown command:", command)
        else:
            print("*** Unknown syntax:", line)

    def handle_update_command(self, class_name, update_command):
        """
        Helper method to handle update command
        """
        instance_id_start = update_command.find("(") + 1
        instance_id_end = update_command.find(")")
        
        if instance_id_start > 0 and instance_id_end > instance_id_start:
            instance_id = update_command[instance_id_start:instance_id_end].strip()
             # Use shlex to properly handle quoted values
            lexer = shlex.shlex(update_command[instance_id_end + 1:], posix=True)
            lexer.whitespace_split = True
            lexer.whitespace += ','
            update_args = f"{class_name} {instance_id} {' '.join(lexer)}"
            self.do_update(update_args)
        else:
            print("*** Invalid update command:", update_command)

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
