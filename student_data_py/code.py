
# Function for data structure making
def student_data(lst_1,lst_2):
    # Combining both listes
    student_dict_ = dict(zip(lst_1,lst_2)) 
    return student_dict_

# list_1 pre-defined with known values
list_1 = ["Name","ENGL101","MATH101","SCI101"]

# initializing second list
list_2 = list()
# list_2 adding with datas
list_2 = list_2 + [input("Enter Name of Student: ")]
list_2 = list_2 + [int(input("Enter Mark of Englis: "))]
list_2 = list_2 + [int(input("Enter Mark of Maths: "))]
list_2 = list_2 + [int(input("Enter Mark of Science: "))]

# returning the data structure in the form of dictionary
print(student_data(list_1,list_2))
