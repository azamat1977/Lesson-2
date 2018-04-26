import re
s = input("The smallest word here is: ")
string = re.findall(r'\S+',s)
print (string)
minlen = min (len(word) for word in string)
print (minlen)
print ([word for word in string if len(word) == minlen])