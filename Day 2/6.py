
import math
def search_prime(n):
    if(n==2):
        return True
    if(n%2==0):
        return False
    i=3
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        i+=2
    return True
def prime_numbers_till_10k():
    prime_list=[]
    for i in range(1,10000):
        if(search_prime(i)):
            prime_list.append(i)
    print(prime_list)
prime_numbers_till_10k()
