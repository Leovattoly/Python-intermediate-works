
# importing required modules 
import argparse 
  
# create a parser object 
parser = argparse.ArgumentParser(description = "A program to validate the Reference ID") 
  
# add argument 
parser.add_argument("refid", nargs = 1, metavar = "Reference ID", type = int,help = "reference ID should be 12 digit without any space") 
  
# parse the arguments from standard input 
args = parser.parse_args() 
  
# argument list is converting to string 
strings = [str(integer) for integer in args.refid]
a_string = "".join(strings)

# check if refid argument has numeric input data. 
#If it has, then checking the size of the data 
# Both cases are true then it's showing its valid reference ID 
if a_string.isnumeric() != False and len(a_string) == 12: 
    print(args.refid+[10]," is validated succesfully") 
else:
    print("Reference id not valid \n")
    