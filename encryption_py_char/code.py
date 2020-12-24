# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:57:16 2020

@author: DELL
"""



def char_value_(c,alpha_lst):
    if c == 'A' or c == 'a' :
        return alpha_lst[0]
    elif (c == 'b' or c == 'B'):
        return alpha_lst[1]
    elif (c == 'C' or c == 'c'):
        return alpha_lst[2]
    elif (c == 'D' or c == 'd'):
        return alpha_lst[3]
    elif (c == 'E' or c == 'e'):
        return alpha_lst[4]
    elif (c == 'f' or c == 'F'):
        return alpha_lst[5]
    elif (c == 'g' or c == 'G'):
        return alpha_lst[6]
    elif (c == 'h' or c == 'H'):
        return alpha_lst[7]
    elif (c == 'i' or c == 'I'):
        return alpha_lst[8]
    elif (c == 'j' or c == 'J'):
        return alpha_lst[9]
    elif (c == 'k' or c == 'K'):
        return alpha_lst[10]
    elif (c == 'l' or c == 'L'):
        return alpha_lst[11]
    elif (c == 'M' or c == 'm'):
        return alpha_lst[12]
    elif (c == 'N' or c == 'n'):
        return alpha_lst[13]
    elif (c == 'N' or c == 'n'):
        return alpha_lst[14]
    elif (c == 'o' or c == 'O'):
        return alpha_lst[15]
    elif (c == 'P' or c == 'p'):
        return alpha_lst[16]
    elif (c == 'Q' or c == 'q'):
        return alpha_lst[17]
    elif (c == 'R' or c == 'r'):
        return alpha_lst[18]
    elif (c == 'S' or c == 's'):
        return alpha_lst[19]
    elif (c == 'T' or c == 't'):
        return alpha_lst[20]
    elif (c == 'U' or c == 'u'):
        return alpha_lst[21]
    elif (c == 'v' or c == 'V'):
        return alpha_lst[22]
    elif (c == 'x' or c == 'X'):
        return alpha_lst[23]
    elif (c == 'y' or c == 'Y'):
        return alpha_lst[24]
    elif (c == 'Z' or c == 'z'):
        return alpha_lst[25]
    else:
        return (0)

alpha_lst = list()
encry_lst = list()
for i in range(1,26): # we can change the encryption terms here
    alpha_lst += [i]
f = open("demofile.txt", "r")
content = f.read()
i = 0
for c in content:
    encry_lst += [char_value_(c,alpha_lst)]
print(encry_lst)