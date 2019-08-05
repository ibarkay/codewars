# coding=utf-8
''' You are given a string where you have to find its first word.

This is a simplified version of the First Word mission.

Input string consists of only english letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string.

Output: A string.

Precondition: Text can contain a-z, A-Z and spaces '''

def first_word(txt):
    txt = txt.split()
    return txt[0]


first_word("Hello world")