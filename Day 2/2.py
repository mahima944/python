
#to find avg of n numbers
def get_avg(a):
    list_size=len(a)
    sum_of_list=0
    for i in a:
        sum_of_list+=i
    return sum_of_list/list_size
def main():
    a=[]
    n = int(input("enter the number of values: "))
    for i in range(n):
        val=int(input(f"enter the value {i+1}: "))
        a.append(val)
    avg=get_avg(a)
    print(f'avg value is: {avg}')
main()
