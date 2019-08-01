# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Adding elements one at a time 
Dict['brand'] = 'Nexa'
Dict['model'] = 'Swift Desire'
Dict['year'] = 2019
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values 
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Updating existing Key's Value 
Dict['model'] = 'Baleno'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict['nested_values'] = {'nested_key' :{'1' : 'value1', '2' : 'value2'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 
