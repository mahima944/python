
def main():
    l1=[]
    print(f'empty list is {l1}')
    l2=[0,1,2,3]
    print(f'list with values {l2}')
    l3=['abc',['xya','cba']]
    print(f'list of list or nested list is {l3}')
    l4=list("spam")
    print(f'list of charecters{l4}')
    l5=list(range(-4,4))
    print(f'the range of numbers are {l5}')
    l6=[1,2,3,4]
    print(f'accesing list by element {l6[1]}')
    l7=['x',[1,2,3],'y']
    print(f'accesing the elelmtn in the list {l7[1][2]}')
    l8=[1,2,3,4,5,6]
    print(f'slicing the list {l8[2:4]}')
    l9=[1,2,3,4,5,6]
    print(f'length of list is {len(l9)}')
    l10=[1,[100,200,300],3,4,5] 
    print(f'slicing the list {l10[1][1:3]}')
    
main()
