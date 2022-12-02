"""
What is the largest prime factor of the number 600851475143 ?

"""
from typing import List
from math import sqrt 

def is_prime(n: int) -> bool: 
    for a in range(2, int(sqrt(n))): 
        if n % a == 0: 
            return False 
    return True 

def largest_prime_factor(x: int) -> int: 
    prime_factors: List[int] = [] 

    for no3 in range(2, int(sqrt(x))): 
        if x % no3 == 0: 
            # no3 and x/no3 are factors of x 
            if is_prime(no3): 
                prime_factors.append(no3) 
            if is_prime(x//no3): 
                prime_factors.append(no3)
                
    return max(prime_factors) 


print(largest_prime_factor(600851475143))
