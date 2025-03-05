
def main():
    nums=int(input("Enter the number of elements in the list: "))
    mylist=[int(input(f"enter the value of{i+1} element: ")) for i in range(nums)]
    mysum=sum(mylist)
    myavg=mysum/len(mylist)
    print(f"Sum of the list is {mysum} {myavg}")  
main()
