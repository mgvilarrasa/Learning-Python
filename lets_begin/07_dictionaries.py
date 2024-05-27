my_dictionay = dict()
my_other_dictionary = {}

my_other_dictionary = {
    "key1":"value1", 
    "key2":"value2", 
    "numericKey":30, 
    "booleanKey":True, 
    1:"valueOnNumericKey"
}

print(my_other_dictionary)

my_dictionay = my_other_dictionary

print(len(my_dictionay))
print(my_dictionay.get("key1"))
print(my_dictionay["key1"])
print(my_dictionay[1])
#print(my_dictionay["nonExistingKey"]) -> Throws error
print(my_dictionay.get("nonExistingKey")) #Returns None
my_dictionay["NewKey"] = "New Value"
print(my_dictionay)

del my_dictionay["key2"]
print(my_dictionay)
my_dictionay.pop("booleanKey")
print(my_dictionay)

print("key1" in my_dictionay)
print("nonExistingKey" in my_dictionay)

print(my_dictionay.items())
print(my_dictionay.keys())
print(my_dictionay.values())
print(my_dictionay.fromkeys(("key1","NewKey"))) #new dict without values

key_list = ["key1", "key2", "key3"]
print(dict.fromkeys(list))