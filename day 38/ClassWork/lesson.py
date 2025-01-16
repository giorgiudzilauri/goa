#CW 1
def manual_difference(set1, set2):
    result = set1.copy() 
    for item in set2:
        result.discard(item)
    return result
 
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

print(manual_difference(set_a, set_b))  

#CW 2
student_1 = {
    "ასაკი": 16,
    "საშუალო ქულა": 85,
    "სახელი": "giorgi",
    "გვარი": "udzilauri"
}

student_2 = {
    "ასაკი": 17,
    "საშუალო ქულა": 70,
    "სახელი": "rezo",
    "გვარი": "qenqadze"
}

print(student_1)
print(student_2)