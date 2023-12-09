#!/usr/bin/python3
"""
entry point of the command interpreter for AirBnB project
"""
import cmd


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
