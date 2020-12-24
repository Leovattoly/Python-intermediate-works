# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:19:09 2020

@author: DELL
"""
import os
try:
    # Read a text fle from the same directory 
    text_file = open('file.txt','r')

    # Printing the content using read method 
    print(text_file.read())
    text_file.close() # close the file
    # Write/append a text fle from the same directory 
    text_file_1= open('file_1.txt','a')
    word_list= ["Game over"]
    text_file_1.writelines(word_list)
    text_file_1.close() # close the file
    desicion = input("Enter Y to delete the file named 'file.txt': ")
    if desicion =='Y':
        os.remove('file.txt')
except ValueError as ve:
    print("Entered value is not acceptable",ve)
    
except TypeError as te:
    print("Entered value is not acceptable",te)
    
except ZeroDivisionError as zde:
    print("Entered value is not acceptable",zde)

except SyntaxError as se:
    print("Syntax Error",se)
    
except RuntimeError as re:
    print("Run time Error",re)

except FileNotFoundError  as fnf:
    print("File not found ",fnf)
except:
    print("An error occured!")
    
finally:
    print('Program exiting.')





