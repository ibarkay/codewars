"""Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.

Example:

checkio(4)=='four'
checkio(143)=='one hundred forty three'
checkio(12)=='twelve'
checkio(101)=='one hundred one'
checkio(212)=='two hundred twelve'
checkio(40)=='forty'"""

def checkio(numy):

   dicto =  {'1':'one',
             '2':'tow',
             '3':'three',
             '4':'four',
             '5':'five',
             '6':'six',
             '7':'seven',
             '8':'eight',
             '9':'nighnth',
             '10':'ten'}

   
   numy = str(numy)
   for i in numy:
       for j in dicto:
           if j in i :
               print dicto[j]
checkio(10)