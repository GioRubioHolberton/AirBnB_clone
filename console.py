#!/usr/bin/python3
'Console implementation'
import cmd


class HBNBCommand(cmd.Cmd):
    'Command interpreter for HBnb Project'
    prompt = "(hbnb) "

    def do_quit(self, args):
        'Exit of the interpreter'
        return (True)

    def do_EOF(self, args):
        'End of File implementation. Exit interpreter'
        return True

    def emptyline(self):
        'Implementation of empty line'
        pass

    def do_create(self, args):
        'Create implementation'
        if len(args) is 0:
            HBNBCommand.error_handler(1)
        else:
            args = args.split()
            if HBNBCommand.verifyclass(args[0]):
                creation = eval(arguments[0])(arguments[1:])
                print(creation.id)
                creation.save()
            else:
                HBNBCommand.error_handler(2)

    def do_show(self, args):
        'Show implementation'
        args = args.split()
        if len(args) is 0:
            HBNBCommand.error_handler(1)
        elif len(args) is 1:
            HBNBCommand.error_handler(4)
        else:
            if HBNBCommand.verifyclass(arguments[0]):
                models.storage.reload()
                elmnts = arguments[0] + "." + arguments[1]
                if elmnts in list(models.storage.all().keys()):
                    print(models.storage.all()[elmnts])
                else:
                    HBNBCommand.error_handler(3)
            else:
                HBNBCommand.error_handler(2)

    def do_destroy(self, args):
        'destroy method'
        args = args.split()
        if len(args) is 0:
            HBNBCommand.error_handler(1)
        elif len(args) is 1:
            if HBNBCommand.verifyclass(arguments[0]):
                HBNBCommand.error_handler(4)
            else:
                HBNBCommand.error_handler(2)
        else:
            if HBNBCommand.verifyclass(arguments[0]):
                models.storage.reload()
                elmnt = arguments[0] + "." + arguments[1]
                if elmnt in list(models.storage.all().keys()):
                    del models.storage.all()[elmnt]
                    models.storage.save()
                else:
                    HBNBCommand.error_handler(3)
            else:
                HBNBCommand.error_handler(2)


if __name__ == '__main__':
    command_prompt = HBNBCommand()
    command_prompt.cmdloop()
