#coding = utf-8
__author__ = "luztak"
__version__ = "0.1"

import sys

class Pyguments(object):
    def __init__(self):
        self.sys_args = sys.args[1:]
        self.commands = {}
        self.used_commands = []
        
        self.parsed = self._parse(self.args)
    
    def add(self, command, cmdtype="normal", function=None, message=None): 
        self.update(command=command, cmdtype=cmdtype, function=function, message=message)
    
    def remove(self, command): 
        del self.commands[command]
    
    def update(self, command, cmdtype="normal", function=None, message=None): 
        if not function:    function = locals().get(command)
        self.commands.update({'command':command, 'cmdtype':cmdtype, 'function':function, 'message':message})

    def getarg(self, command):
        cmdtype = self.commands[command]["cmdtype"]
        if cmdtype == "normal" or cmdtype == "hyphen" or cmdtype == "long": #python a.py test/-t/--time-max
            arg = None
        elif cmdtype == "normalafter" or cmdtype == "hyphenafter": #python a.py t60/-t60
            for cmd in seld.sys_args:
                if cmd[:len(command)] == command:
                    arg = cmd[len(command):]
        elif cmdtype == "hyphenspace" or cmdtype == "longspace": #python a.py -t 60/--time-max 60
            arg = self.sys_args[self.sys_args.index(command) + 1]
        return arg
    
    
    def _parse(self, args): 
        parsed = []
        for arg in args: 
            pass
    
    
    def __getitem__(self, command):
        return self.commands[command]
    
    def __setitem__(self, command, args):
        self.commands[command] = args
    
    def __delitem__(self, command):
        del self.commands[command]
