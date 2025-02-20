#we have HW in Codewars


#HW 1
def simple_multiplication(number) :
    if number % 2 == 0:
        return number *8
    else:
        return number *9
    
#HW 2
def invert(lst):
    return [-x for x in lst]

#HW 3
def fake_bin(x):
    result = ""
    
    for digit in x:
        num = int(digit)
        
        if num < 5:
            result += "0"
        else:
            result += "1"
    
    return result

#HW 4
def string_to_array(s):
    return s.split()

#Hw 5
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    winning_cases = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_cases[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
#hw 6
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
    
#HW 7
def monkey_count(n):
    return list(range(1, n + 1))

#HW 8
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    
    elif human_years == 2:
        return [2, 24, 24]
    
    cat_years = 24 + (human_years - 2) * 4
    dog_years = 24 + (human_years - 2) * 5
    
    return [human_years, cat_years, dog_years]

#Hw 9
def is_isogram(string):
    string = string.lower()
    
    seen = set()
    
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    
    return True

#HW 10
def binary_array_to_number(arr):
    return int(''.join(map(str, arr)), 2)