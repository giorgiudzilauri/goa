# classwork 1

def greet(s):
    return "hello world!"

# classwork 2

def repeat_str(repeat, string):
    return string * repeat

# classwork 3

def no_space(x):
    #your code here
    return x.replace(" ", "")

# classwork 4

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+= [i]
        i += 1
    return res

# classwork 5

def maps(a):
    arr = []
    
    for i in a:
        arr.append(i * 2)
        
    return arr

# classwork 6

def grader(s):
    if s > 1 or s < 0.6:
        return "F"
    elif s >= 0.9:
        return "A"
    elif s >= 0.8:
        return "B"
    elif s >= 0.7:
        return "C"
    elif s >= 0.6:
        return "D"
    
# classwork 7

websites = []
for index in range(0,1000):
    websites.append("codewars")

# classwork 8