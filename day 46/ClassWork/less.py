#we have Classwork in codewars

#task 1
def filter_list(l):
    print(f"Original list: {l}")  
    result = [x for x in l if isinstance(x, int)]
    print(f"Filtered list: {result}")  
    return result


#task 2
def disemvowel(string):
    return ''.join(i for i in string if i not in "aeiuoAEIOU")

#task 3
def descending_order(num):
    num_str = str(num)
    digits = []

    
    for digit in num_str:
        digits.append(digit)
    
    digits.sort(reverse=True)

    return int(''.join(digits))