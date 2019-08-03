# Initial Dictionary 
Dict = { 5 : 'Value-5', 6 : 'Value-6', 7 : 'Value-7', 
		'A' : {1 : 'Value-1', 2 : 'Value-2', 3 : 'Value-3'}, 
		'B' : {1 : 'Value-4', 2 : 'Value-5'}} 
print("Initial Dictionary: ") 
print(Dict) 

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

# Deleting a Key from Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 

# Deleting a Key using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 

# Deleting Key-value pair using popitem() 
# The popitem() method removes the item that was last inserted into the dictionary.
# In versions before 3.6, the popitem() method removes a random item. The removed i
Dict.popitem() 
print("\nPops a key-value pair: ") 
print(Dict) 

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 
