# zip() in python
# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity. 

# Initializing the list
name = ["Nitin", "Nikit", "Nikhil", "Nitesh"]
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ]

# using zip() to map values 
mapped = zip(name, roll_no, marks)

print(mapped)

# converting values to print as list 
mapped = list(mapped) 

# converting values to print as set 
# mapped = set(mapped)

# printing resultant values  
print ("The zipped result is : ") 
print (mapped)

# How to unzip?
# Unzipping means converting the zipped values back to their original format as they were. This is done with the help of “*” operator.

# unzipping values 
name_, roll_no_, marks_ = zip(*mapped)

# printing initial lists 
print("The name list is : ", name_) 

print("The roll_no list is :", roll_no_) 
  
print("The marks list is : ", marks_) 

