# The time module comes with Python’s standard utility module,
# so there is no need to install it externally. We can simply
# import it using the import statement.
# import time

#usage of time module:
# Python has defined a module, “time” which allows us to handle various operations regarding time,
# its conversions and representations, which find its use in various applications in life.
# The beginning of time is started measuring
# #display the programs to usage of it:
import time
# initial = time.time()
# for i in range(45):   #using for loop
#     print("banglore is beautiful")
# print(time.time()-initial, "seconds")
#
# initial2 = time.time() #using while loop
# k=0
# while(k<45):
#     print("banglore is beautiful")
#     k=k+1
# print(time.time()-initial2, "seconds")

#3 type time sleep
# for i in range(45):
#      print("banglore is beautifull")
#      time.sleep(2)

# import time
# ti = time.gmtime()
# # using asctime() to display for using current time
# print("Time calculated using asctime() is : ", end="")
# print(time.asctime(ti))

# # using ctime() to display time string using seconds
#in time.ctime() method converts a time in seconds
# import time
# print("Time calculated using ctime() is : ", end="")
# print(time.ctime(2456326.67899))