max_iteration = 5
count = 0
while count < max_iteration:
    print("Loop number", count+1)
    if count == 3:
        print("Found it!")
        break
    count += 1

number_list = [12, 25, 17, 68, 23, 109, 1023, 888, "Test"]

for item in number_list:
    print(f"Current item {item}")
    if item == 109:
        print("Found 109")
        continue
    if item == "Test":
        print("Found Test") 