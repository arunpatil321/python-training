#regular expresions means that it is a special characters that define the pattern matching
#in the given string
#regular expressions are used to check wether the specified pattern present in the given string or not
#real time example : google pay phone pay
#source(par1,par2)

#where we can use reglar expressions:
#we can use to extract inforamation
#where ever we pass some information we can extracting information
#how to implement reguar expresions for using ?
#for using re module it is apredefined regukar expresions
#re is a module it is a collection of predefined function
#what is the use of it?
#just we can extract to process or validate inpur text or string.

#they having number of functions:
#match():to test input strings start with pattern or not specified.
#search():just to specifid pattern is present or not in given input or text.
#findall():to find duplicates for specifed pattern it can check the duplicates values.
#split():it can just split the input string:
#sub():replace the substrings:
#compile():used to create pattrn object and can be reused.
# import re
# line="python and java gives jython"
# r1=re.match(r"python",line)
# print(r1)
# print("\n")
#another way to write the program
# import re
# line="python and java gives jython"
# found=re.match(r"python",line)
# if found:
#     print("match found")
# else:
#     print("not found")

# import re
# #Split the string at every white-space character:
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)


