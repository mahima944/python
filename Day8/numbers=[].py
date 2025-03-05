numbers=[]
def second_largest(numbers):
    largest = second_largest = float('-inf')
    for i in range(len(numbers)):
        if(numbers[i]>largest):
            second_largeest=largest
            largest=numbers[i]
        if(numbers[i]>second_largest and numbers[i]<largest):
            second_largest=numbers[i]
            
    return second_largest
            