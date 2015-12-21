# word-addition.py
# by Rick Elwood
# 12-20-2015
# reads from dictionary of words and finds words that
# when added together result in another. Assuming base
# 27 addtion 0 = ' ' to 26 = 'z' lowercase only.

import sys
from binascii import *

BASE27LOOKUP = ' abcdefghijklmnopqrstuvwxyz'

def add_words(word_1, word_2):

    # pad the smaller string with leading zeros ('`' in this case)
    # save the length of the longest string
    if len(word_1) > len(word_2):
        length = len(word_1)
        word_2 = word_2.rjust(length,'`')
    elif len(word_2) > len(word_1):
        length = len(word_2)
        word_1 = word_1.rjust(length,'`')
    else:
        length = len(word_1)

    # convert unicode strings to byte arrays
    word_2 = word_2.encode()
    word_1 = word_1.encode()
    result = ""
    letter_sum = 0
    carry = 0

    # iterate through the strings backwards adding each character and performing a carry if needed
    i = length -1
    while (i >= 0):
        letter_sum = (word_1[i] + word_2[i] + carry) - 96
        if letter_sum > ord('z'):
            letter_sum-=27
            carry=1
        else:
            carry = 0
        if letter_sum == 96:
            letter_sum = 32
        result = chr(letter_sum) + result
        i -= 1
    if carry == 1:
        result = 'a' + result
    print(result)


add_words('zog', 'catamaran')

