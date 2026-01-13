#!/usr/bin/python3
from importlib import util
import sys
if __name__ == "__main__":
    module = ""
    spec = util.spec_from_file_location(module, "/tmp/hidden_4.pyc")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for i in dir(module):
        if i[0] != '_':
            print("{}".format(i))
        
    
