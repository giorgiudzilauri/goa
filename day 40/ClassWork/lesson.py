#we have py in codewars

#1 problem
def password(st):
    has_upper = False
    has_lower = False
    has_digit = False
    
    if len(st) < 8:
        return False
    
    for char in st:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if has_upper and has_lower and has_digit:
        return True
    
    return False

#2 problem
def is_isogram(string):
    lowerd_string= string.lower()
    for char in lowerd_string:
        if lowerd_string.count(char) > 1:
            return False
    return True

#3 problem
def friend(x):
    list_friends = []

    for i in x:
        if len(i) == 4:
            list_friends.append(1)
    return list_friends

#4 problem
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for char in pin:
            if not char.isdigit():
                return False
        return True
    return False

print(validate_pin("1234"))   
print(validate_pin("12345"))  
print(validate_pin("a234"))   
print(validate_pin("123456")) 


