import re

test_string = "This is test text num. 1"
another_test_string = "Another test text num. 2"
#re.match() -> matching string from start
print(re.match("This", test_string))
print(re.match("This", another_test_string))
print(re.match("test", test_string))

test_regex = re.match("This is", test_string, re.I)
print(test_regex)
print(test_regex.span())
start, end = test_regex.span()
print(test_string[start:end])