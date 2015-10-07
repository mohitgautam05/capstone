f = open('C://input.txt')  
lines = f.readlines()  # return a list of lines in file

list_of_elements = []
for line in lines:
    list_of_elements += line.split()

f.close()
print (list_of_elements)