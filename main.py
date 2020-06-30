def fizz_buzz(number):
    '''Function checks is input numer devided by 3, 5
     or both same time.
     
     Args:
     number (int)

     Returns:
     "FizzBuzz" when devided by 3 and 5 (15 in total)
     "Fizz" when devided by 3 but not 5.
     "Buzz" when devided by 5 but not 3
     '''
    if number % 15 == 0:
        result = 'FizzBuzz'
    elif number % 5 == 0:
        result = 'Buzz'
    elif number % 3 == 0 :
        result = 'Fizz'
    else:
        result = number

    return result


def input_int(massage):
    '''Function bases on input function. Checks is the input int type
    
    Args:
        massage (string): message that has to be printed.

    Returns:
        formatted input to int.
    '''
    while True:
        got = input(massage)
        try:
            int_number = int(got)
            break
        except ValueError:
            print("It's not a number, select it once more !")
    return int_number


def main():
    '''Function asks for numbers, checks condition 1 <= n < m <= 10000,
    run loop and function fizz_buzz'''
    while True:
        n = input_int('Select first number: ')
        if 1 <= n < 10000:
            break
        else:
            print('It should be between 1 and 9999 !')
    
    while True:
        m = input_int('Select second number, grater than n: ')
        if n < m <= 10000:
            break
        else:
            print('It should be between n and 10000 !')

    for number in range(n, m + 1):
        print(fizz_buzz(number))


if __name__ == '__main__':
    main()