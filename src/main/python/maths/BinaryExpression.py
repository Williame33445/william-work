# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

from maths.Constant import Constant
from maths.Expression import Expression

class BinaryExpression(Expression):       #This class a several sub classes that it runs to 
    def __init__(self,l,r,symbol):
        def asExpression(x):
            if isinstance(x,Expression):
                return x
            else:
                return Constant(x)
            
        self.leftExpression = asExpression(l)
        self.rightExpression = asExpression(r)
        self.symbol = symbol
        
    def leftEvaluated(self):
        return self.leftExpression.evaluate()
    def rightEvaluated(self):
        return self.rightExpression.evaluate()
        
    def __str__(self):  #called by python when it tries to convert the object to a string
        return "(" + str(self.leftExpression) + " " + self.symbol + " " + str(self.rightExpression) + ")"
            
    def __eq__(self, other):    #called by python when two objects == each other
        return isinstance(other, BinaryExpression) and self.leftExpression == other.leftExpression and self.rightExpression == other.rightExpression and self.symbol == other.symbol