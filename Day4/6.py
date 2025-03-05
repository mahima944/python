
def get_input():
    str=input("enter a string")
    return str
def remove_extra_spaces(str):
    count_space=0
    new_str=''
    for i in str:
        if(i==" "):
            count_space+=1
            if(count_space>=2):
                continue
        else:
            count_space
        new_str+=i
    return new_str
def main():
    str=get_input()
    newstr=remove_extra_spaces(str)
    print(str)
    print(newstr,sep="-")
main()
