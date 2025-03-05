import threading
import time
def print_odd(numbers, result, index):
    time.sleep(2)  
    odd_numbers = [num for num in numbers if num % 2 != 0]
    result[index] = odd_numbers
    print(f"Odd numbers: {odd_numbers}")

def print_even(numbers, result, index):
    time.sleep(2)  
    even_numbers = [num for num in numbers if num % 2 == 0]
    result[index] = even_numbers
    print(f"Even numbers: {even_numbers}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = [[], []]


thread_odd = threading.Thread(target=print_odd, args=(numbers, result, 0))
thread_even = threading.Thread(target=print_even, args=(numbers, result, 1))


thread_odd.start()
thread_even.start()


thread_odd.join()
thread_even.join()


print(f"Final Odd Numbers: {result[0]}")
print(f"Final Even Numbers: {result[1]}")
