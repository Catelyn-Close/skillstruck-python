#python libraries also have datetime which allows working with dates and times
import datetime
x = datetime.datetime.now() #doesnt exist??
print(x.strftime("%X"))
#%X means to the second for time in a str format
x = datetime.date.now()
today = datetime.date.today()
#gen a date in str form
#%m makes is a two number month 03 != 3
#same for %d but for day 02 - 2
#gen 4 digit year as str %Y

#checkpoint
print(x.strftime("%X"))
print(x)
print(today)
print(x.strftime("%m"))
print(x.strftime("%d"))
print(x.strftime("%Y"))
#challenges
