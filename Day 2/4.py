

#to find greatest among 3 numbers
def get_input():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=int(input("enter third number: "))
    return a,b,c
def find_max(a,b,c):
    max=-1
    if(a>b and a>c):
        max=a
    elif(b>c):
        max=b
    else:
        max=c
    return max

def main():
    a,b,c=get_input()
    max_value=find_max(a,b,c)
    print(f"max value is: {max_value}")
main()
