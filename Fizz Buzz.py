def checkio(number):
    if number%3 is 0 :
        if number%5 is 0:
            return 'Fizz Buzz'
        else:
            return 'Fizz'
    if number%5 is 0:
        if number%3 is not 0:
            return 'Buzz'

    if number%3 is not 0:
        if number%5 is not 0:
            return str(number)



checkio(7)





'''"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.'''