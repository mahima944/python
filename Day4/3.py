
import math
def search_prime(n):
    if(n==1):
        return False
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
    prime_list=[i for i in range(1000) if(search_prime(i))]
    print("the smallest prime number is ",prime_list[0])
    print("the largest prime number is ",prime_list[-1])
prime_numbers_till_10k()
