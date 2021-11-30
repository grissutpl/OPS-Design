# -*- coding: utf-8 -*-
"""
Created on Wed Jan 01 20:00:29 2020 

@author: Ing. Daniel Villarreal
"""

import sys, os

class Logger(object):
    """
    Lumberjack class - duplicates sys.stdout to a log file and it's okay
    source: https://stackoverflow.com/a/24583265/5820024
    """
    def __init__(self, filename="Prints_k", mode="wb", buff=0): # https://stackabuse.com/file-handling-in-python/
        self.stdout = sys.stdout
        self.file = open(filename, mode, buff)
        sys.stdout = self
    
    def __del__(self):
        self.close()
    
    def __enter__(self):
        pass
    
    def __exit__(self, *args):
        pass
    
    def write(self, message):
        self.stdout.write(message)
        self.file.write(message.encode("utf-8"))
    
    def flush(self):
        self.stdout.flush()
        self.file.flush()
        os.fsync(self.file.fileno())
    
    def close(self):
        if self.stdout != None:
            sys.stdout = self.stdout
            self.stdout = None
    
        if self.file != None:
            self.file.close()
            self.file = None