#This code reverses a given string.

def string_reverse(text):
    string_reverse=""
    num=len(text)-1
    
    for n in text:
        string_reverse += text[num]
        num-=1
        
    return string_reverse   
