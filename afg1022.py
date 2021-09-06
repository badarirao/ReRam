# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:47:30 2021

@author: Badari
"""

from pyvisa import ResourceManager

class AFG1022:
    def __init__(self,adapter,**kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            inst = rm.open_resource(adapter)
            self.inst = inst
        
    def getinfo(self):
        print(self.inst.query('*IDN?'))
    
    def ask(self,cmd):
        self.inst.query(cmd)
    
    def write(self,cmd):
        self.inst.write(cmd)
    
    def read(self):
        self.inst.read()