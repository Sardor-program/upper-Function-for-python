# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Lower_To_Upper = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 
'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 
'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 
'X', 'y': 'Y', 'z': 'Z'}
    
def getUppercase(text):
    uppercaseText = ''    
    for charachter in text:
        if charachter in Lower_To_Upper:
            uppercaseText += Lower_To_Upper[charachter]
        else:
            uppercaseText += charachter
            
    return uppercaseText        
    
    
    