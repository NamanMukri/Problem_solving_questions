
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
def num():       
    x=1    
    while True:
        count=0        
        y=1
        for y in range(1,21):
            if x%y!=0:
                x+=1                                
                break
            else:
                y+=1
                count+=1
        if count==20:
            break
    return (x)
print(num()) 
            
            
        
            


    
        



  

        
    
    