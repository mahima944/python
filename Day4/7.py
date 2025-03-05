
def get_input():
    nums=int(input("Enter the number of elements in the list: "))
    mylist=[int(input(f"enter the value of{i+1} element: ")) for i in range(nums)]
    return mylist
def smallest_element(mylist):
    return sorted(mylist)[0]
def largest_element(mylist):
    return sorted(mylist)[-1]
def main():
    mylist=get_input()
    print(f'the smallest element is {smallest_element(mylist)}')
    print(f'the largest element is {largest_element(mylist)}')
main()
