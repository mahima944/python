
#to find avg of 4 numbers
def get_input():
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    num3=int(input("enter third number: "))
    num4=int(input("enter fourth number: "))
    return num1,num2,num3,num4
def get_avg(num1,num2,num3,num4):
    avg=(num1+num2+num3+num4)/4
    return avg
def main():
    print("enter 4 numbers: ")
    (num1,num2,num3,num4) = get_input()
    avg=get_avg(num1,num2,num3,num4)
    print("average of 4 numbers is: ",avg)

main()
