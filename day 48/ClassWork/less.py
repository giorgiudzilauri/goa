#We have CodeWars

#CW 1
def xo(s):
    x_raodenoba = s.lower().count('x')
    o_raodenoba = s.lower().count('o')
    
    if x_raodenoba == o_raodenoba:
        return True
    else:
        return False
    
#CW 2
def find_short(s):
    words = s.split()  
    lengths = [len(word) for word in words]  
    return min(lengths) 

#CW 3
def solution(text, ending):
    if text[-len(ending):] == ending:
        return True
    else:
        return False

#CW 4
def accum(s):
    result = []  
    for i, c in enumerate(s):
        result.append(c.upper() + c.lower() * i)  
    return '-'.join(result)