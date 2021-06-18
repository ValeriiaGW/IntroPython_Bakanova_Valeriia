####################################################################
#1
value = 167
value = int(value)
new_value = str(value / 2)  if value < 100 else str(value)[::-1]
print(new_value)
#######################################################################
#2
value = 99
value = int(value)
new_value = 1 if value < 100 else 0
print(new_value)
#######################################################################
#3
value = 344
value = int(value)
new_value = True if value < 100 else False
print(new_value)
#######################################################################
#4
my_str = "qwqwTYYfw"
my_str = my_str.upper()
print(my_str)
#######################################################################
#5
my_str = "jkhkUuGUGGJVB"
my_str = my_str.lower()
print(my_str)
#######################################################################
#6
my_str = "qwer"
new_str = my_str if len(my_str) >= 5 else my_str * 2
print(new_str)
#######################################################################
#7
my_str = "qwer"
new_str = my_str if len(my_str) >= 5 else my_str + my_str[::-1]
print(new_str)