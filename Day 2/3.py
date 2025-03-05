
def get_values():
    a=int(input("enter first number: "))
    maxval=a
    chat='a'
    b=int(input("enter second number: "))
    if(b>maxval):
        maxval=b
        char='b'
    c=int(input("enter third number: "))
    if(c>maxval):
        maxval=c
        char='c'
    return a,b,c,maxval,char
def main():
    a,b,c,maxval,char=get_values()
    print(f"max value is: {maxval} and the value is {char}")
main()
