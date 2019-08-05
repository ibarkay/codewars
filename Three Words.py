'''Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

Example:

checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False'''

def checkio(txt):
    counts = ''
    splitlist = txt.split()

    for i in splitlist:
        if i[0].isalpha():
            counts +='1'
        else:
            counts +='0'

    if '111' in counts:
        return True
    else:
        return False






checkio("Hello World hello")