#This function takes an input and finds character frequency#

def character_frequency():   
    
    string=input("Enter string:")   
    
    dict={}   
    
    for charater in string:       
        
        keys=dict.keys()       
        
        if charater in keys:          
            
            dict[charater]+=1          
            
        else:            
            
            dict[charater]=1
            
    return dict
