
def user_input():
    str = input("Enter a string to check if palindrome or not: ")
    return str

def is_palindrome(mylist):
    list_size = len(mylist)
    first_half = mylist[:list_size//2]  # Corrected to integer division
    second_half = mylist[-(list_size//2):]  # Correct slicing to get the second half
    i=0
    bool=False
    print(first_half)
    print(second_half)
    while i<len(first_half):
        if(first_half[i]==second_half[-(i+1)]):
            bool = True
        else:
            bool = False
        i+=1
    return bool

def main():
    str = user_input()
    mylist = list(str)
    print(is_palindrome(mylist))
main()
