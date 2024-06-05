import os
import json

#TXT
'''
txt_file = open("some_more/test_file.txt", "r+")
print(txt_file.read())         #Reads all the file
print(txt_file.read(10))       #Reads N characters
print(txt_file.readline())     #Reads first line
print(txt_file.readlines())     #Returns an array with all lines, each is an string

txt_file.write("\nThis is an added line")
print(txt_file.read())

second_txt_file = open("some_more/test_file2.txt", "w+")
second_txt_file.write("This is a new file")
print(second_txt_file.readlines())
second_txt_file.close()
os.remove("some_more/test_file2.txt")
'''
#JSON WRITE
'''
json_file = open("some_more/test_file.json", "w+")

json_text = {
    "name": "TestName",
    "surname": "TestSurname",
    "age": 35,
    "is_active": True
}

json.dump(json_text, json_file, indent=4)
'''
#JSON READ
json_file = open("some_more/test_file.json", "r+")
json_object = json.load(json_file)
print(json_object)