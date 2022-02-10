#HOW TO USE DATE AND TIME MODULE
import datetime
cd=datetime.datetime.now() #RETRIVING CURRENT DATE AND TIME
# print(cd)
# x=datetime.datetime(2020,6,8) #we can creating datetime
# print(x)
# a=cd.strftime("%Y")
# print("short version of year:",a)

a=cd.strftime("%b")
print("full version of month:",a)

# a=cd.strftime("%A")
# print("full version  of day:",a)

# a=cd.strftime("%H")
# print("24 HOURS FROMMAT:",a)

# a=cd.strftime("%I")
# print("12HOURS FROMMAT:",a)





