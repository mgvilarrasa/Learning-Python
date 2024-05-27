condition = True
if(condition):
    print("We are in!")
else :
    print("Not quite yet!")
print("Last one")

condition_2 = 9
if(condition_2 >= 10):
    print("Large!")
elif(condition_2 > 5 and condition_2 < 10):
    print("Medium")
else:
    print("Small")

some_text = ""
if not some_text:
    print("Empty text")
elif(some_text == "This text"):
    print("Matching text")
else:
    print("No clue")