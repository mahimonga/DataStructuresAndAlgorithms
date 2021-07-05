a, b = [int(i) for i in input().split()]
    
def GCD(a, b): 
    while(b):
        a, b = b, a % b 
        
    return a 
  
print (GCD(a,b)) 