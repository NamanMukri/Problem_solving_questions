"""The prime factors of 13195 are 5, 7, 13 and 29.

     What is the largest prime factor of the number 600851475143 ?"""
number=12
prime_fact=[]
num=2
while num*num<=number:
     if number%num:
          num=+1
     else:                        
          divi=number//num
          prime_fact.append(num)
          number=divi
          print(number)
          
          
     
print("The largest prime factor of 600851475143 is ", prime_fact)

# def largest_prime_factor(n):  
#     i = 2  
#     while i * i <= n:  
#         if n % i:  
#             i += 1  
#         else:  
#             n //= i  
#     return n  
  
# print(largest_prime_factor(5))  