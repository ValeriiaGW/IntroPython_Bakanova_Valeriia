www = 'www.google.com'
if "com" in www:
    print("com in www")
else:
    print("com not in www")
#############################
www = 'www.command_and_conquer.com'
if "com" in www:
    print("com in www")
else:
    print("com not in www")
###########################
www = 'www.command_and_conquer.net'
if "com" in www:
    print("com in www")
else:
    print("com not in www")
###########################
www = 'www.command_and_conquer.net'
if ".com" in www:
    print("com in www")
else:
    print("com not in www")
#############################
www = 'www.conquer_and_command.net'
if".com" in www:
    print("com in www")
else:
    print("com not in www")
#################################
value = 123
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)
################################
value = 321
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)
##############################
value = 123
my_str = str(value) if value < 200 else str(value)[::-1]
print(my_str)
###############################
value = 321
my_str = str(value) if value < 200 else str(value)[::-1]
print(my_str)
##############################
value = "123456789"
my_str = value if len(value) < 5 else value[2:5]
print(my_str)
##############################
value = "123456789"
my_str = value if len(value) >= 5 else value[2:5]
print(my_str)
##############################
value = "123456789"
my_str = value if len(value) < 5 else value[2:5:2]
print(my_str)
#############################
value = "123456789"
my_str = value if len(value) >=5 else value[2:5:2]
print(my_str)
##############################
value = "123456789"
my_str = value if len(value) <= 5 else value[2:5]
print(my_str[::-1])
##############################
value = "123456789"
my_str = value if len(value) >= 5 else value[2:5]
print(my_str[::-1])
#############################
value = "123456789"
my_str = value if len(value) <= 5 else value[2:5:2]
print(my_str[::-1])