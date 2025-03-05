
def main():
    print("the fibonacci series is: ")
    first=0
    second=1
    i=0
    print(f"{first} {second}",end="")
    while(i<10):
        new=first+second
        print(f" {new}",end="")
        first=second
        second=new
        i+=1

main()
