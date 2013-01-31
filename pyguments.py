#coding = utf-8
__author__ = "luztak"
__version__ = "0.1"

import sys

class Pyguments(object):
    def __init__(self):
        self.sys_args = sys.args[1:]
        self.commands = {}
        self.used_commands = []
        
        self._parse_sys_args()
    
    def add(self, command, cmdtype="normal", function=None, message=None): 
        if not function:    function = getattr(__name__, command)
        #this getattr is wrong.needs solution.
        self.commands.update({'command':command, 'cmdtype':cmdtype, 'function':function, 'message':message})
    
    def remove(self, command): 
        del self.commands[command]
    
    def update(self, command, cmdtype="normal", function=None, message=None): 
        self.add(command, cmdtype=cmdtype, function=function, message=message)

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
    
    
    def __getitem__(self, command):
        return self.commands[command]
