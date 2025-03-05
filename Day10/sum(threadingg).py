import threading
import time
def sum_part(number, result, index):
    time.sleep(2)
    result[index] = number
    print(f"Part of sum: {number}")
   

def main():
    num1 = 5
    num2 = 10
    result = [0, 0]  

    thread_1 = threading.Thread(target=sum_part, args=(num1, result, 0))
    thread_2 = threading.Thread(target=sum_part, args=(num2, result, 1))

    thread_1.start()
    thread_2.start()

    
    total_sum = sum(result)

    print(f"Total sum: {total_sum}")

if __name__ == "__main__":
    main()
