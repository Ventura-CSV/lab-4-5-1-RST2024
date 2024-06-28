import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
   
    i = 0
    total = 0
    numbers = [0] * 5
    print(numbers)
    while i < 5:
        number = random.randint(0,100)
        numbers[i] = number
        total = total + number
        i = i + 1
        
    
    

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
