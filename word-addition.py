# word-addition.py
# by Rick Elwood
# 12-20-2015
# reads from dictionary of words and finds words that
# when added together result in another. Assuming base
# 27 addition 0 = ' ' to 26 = 'z' lowercase only.

import time

p=0
# Adds two words and returns the result as a string
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
    global p
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
    if k > p:
        print(k)
        p = k
    return result

# open the input text file and add words to list
with open('wordlist.txt') as f:
    wordlist = [wordlist.rstrip('\n') for wordlist in open('wordlist.txt')]

# create output text file to store the words that result in a valid word
results_file = open('word_sum_results.txt', 'w')
dict_length = len(wordlist)
word_count = k = j = 0
start_time = time.time()
print("Completed: ", end='', sep='')
while k < dict_length:
    j = k
    while j < dict_length:
        word_sum = add_words(wordlist[k], wordlist[j])
        if word_sum in wordlist:
            word_count +=1
            result_string = '\n' + str(word_count) + ': ' + wordlist[k] + ' + ' + wordlist[j] + ' = ' + word_sum + '\n'
            results_file.write(result_string)
        j = j + 1
    time.sleep(1)
    k += 1
f.close()
print('total matches: ', word_count)
print('time:',time.time() - start_time)


