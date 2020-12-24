def main():
    file1 = open("dognames.txt","r+") 
    file2 = open("catnames.txt","r+")
    if(file1 and file2 ):

        # printing the contents of the both files

        print("\n Dogs name file content \n")
        print (file1.read()) 
        print("\n Cats name file content \n")
        print (file2.read()) 
        file1.close()
        file2.close()
        # Adding content to cat names file
        file3 = open("catnames.txt","a")
        file3.write("\n Sassy \n Lucy") 
        file3.close()
        file2 = open("catnames.txt","r+")

        print("\n Cats name file content (after appending)\n")
        print (file2.read())
    else:
        print("Unable to access one or more files")

main()






