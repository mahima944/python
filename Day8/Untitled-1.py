def display(data):
    print(f" the data is{data}")
    
def get_input():
    data=input("enter the data")
    return data
    
def add_num(list):
    num=int(input("enter the number to add into list"))
    list.append(num)

def remove_num(list):
    num=int("enter the number to remove from list")
    for i in range(len(list)):
        if list[i]== num:
            list.pop(i)
            print(f"{num} has been removed from the lsit")
        else:
            print(f"{num} is not found in the list")

def reverse(list):
    n=len(list)
    for i in range(n//2):
       list[i],list[n-i-1]=list[n-i-1], list[i]
    print("list has been reversed")


def second_largest(list):
    largest = second_largest = float('-inf')
    for i in range(len(list)):
        if(list[i]>largest):
            second_largeest=largest
            largest=list[i]
        if(list[i]>second_largest and list[i]<largest):
            second_largest=list[i]
            
    return second_largest
            
    
def main():
    list=[]
    while True:
        print("1.add number")
        print("2.remove number")
        print("3.reverse")
        print("4.second largest")
        print("5.exit")
        
    choice=input("enter your choice (1-4)")
    if choice=='1':
        add_num(list)
        
    elif choice=='2':
        remove_num(list)
        
    elif choice=='3':
        reverse(list)
    
    elif choice=='4':
        list.append(second_largest())
        
    else:
        print("invalid choice")
        
        
main()