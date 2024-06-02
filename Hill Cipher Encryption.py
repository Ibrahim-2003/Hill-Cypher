import os
import string
import numpy as np
import random
from random_word import RandomWords
os.system('color a')

alpha_num_dictionary = dict(zip(string.ascii_lowercase, range(0,26)))
num_alpha_dictionary = dict(zip(range(0,26), string.ascii_lowercase))

names = ['issa', 'anas', 'ali', 'hamada', 'osama',
        'omar', 'ammar', 'ibrahim', 'mohammad', 'mohammed',
        'aliriza', 'yasmin', 'fatima', 'zayneb', 'maryam',
        'yusuf', 'yassine', 'Jon', 'Bill', 'Maria', 'Jenny', 'Jack',
        'abdallah', 'abdula', 'abdulrahman', 'abdelwahhab', 'abdalaziz',
        'salman', 'hashim', 'mahmoud', 'mahmood', 'faisal', 'hussam',
        'husam', 'majid', 'majd', 'zaid', 'ahmad', 'ahmed', 'karam',
        'kareem', 'jackson', 'steve', 'sayid', 'said', 'qasim', 'qusai',
        'nabeel', 'nabil', 'bilal', 'abubakr', 'badr', 'layla', 'lameece',
        'salam', 'salim', 'samhar', 'faris', 'farris', 'saif', 'tayseer',
        'thaer', 'ismail', 'ismael', 'jibreel', 'ishaaq', 'yaqoob', 'dawood',
        'musa', 'yunis', 'science', 'wael', 'jasim', 'habib', 'haywan',
        'hemar', 'achraf', 'karim', 'mehmet', 'uthman', 'obaidah', 'khalil',
        'khalid', 'khaled', 'shuayb', 'uzair', 'idris', 'saleh', 'salah',
        'sahal', 'samer', 'nuh', 'harun', 'raqeeb', 'ateed', 'yazan', 'majed'
        'musallam']

def alpha_to_num(x):
    #USE AN ITERATION OF PLAINTEXT LIST -> THIS LOOKS THROUGH THE LIST AND RETURNS LIST FOR EACH PAIR
    #EXAMPLE:
    # for num in range(len(plaintext_list)):
    #   print(alpha_to_num(plaintext_list[num]))
    new_pair = []
    for y in x:
        for letter in y:
            letter_list = []
            letter_list.append(alpha_num_dictionary[letter.lower()])
            new_pair.append(letter_list)
    return new_pair

def key_alpha_to_num(x):
    #USE AN ITERATION OF PLAINTEXT LIST -> THIS LOOKS THROUGH THE LIST AND RETURNS LIST FOR EACH PAIR
    #EXAMPLE:
    # for num in range(len(plaintext_list)):
    #   print(alpha_to_num(plaintext_list[num]))
    new_pair = []
    for y in x:
        for letter in y:
            new_pair.append(alpha_num_dictionary[letter.lower()])
    return new_pair



def inverse_mod(y):
    answer = pow(y, -1, 26)
    return answer

def mod(y):
    answer = y%26
    return answer


#plaintext = RandomWords().get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb")
plaintext = random.choice(names)
key = ''
key += 'LION'
print('Your randomized key is: LION')


plaintext = plaintext.upper()
key = key.upper()

plaintext_list = []
key_list = []

if len(plaintext)%2 != 0:
    plaintext += 'z'
for letter in plaintext:
    if letter == '-':
        plaintext.replace('-','z')


for num in range(0,len(plaintext),2):
    plaintext_list.append(plaintext[num] + plaintext[num+1])

for num in range(0,len(key),2):
    key_list.append(key[num] + key[num+1])

#print(plaintext_list)


#print(key_list)

key_matrix = []

for num in range(len(key_list)):
    key_matrix.append((key_alpha_to_num(key_list[num])))

#print(key_matrix)

encoded_cipher = ''

for num in range(len(plaintext_list)):
    cipher_matrix = mod(np.matmul(key_matrix, alpha_to_num(plaintext_list[num])))
    #print('---------')
    #print(cipher_matrix)
    cipher = ''
    for matrix in cipher_matrix:
        cipher += num_alpha_dictionary[matrix[0]]
    encoded_cipher += cipher.upper()
    #print(cipher)

print('Your cipher is: ')
print(encoded_cipher)

input('Press enter to reveal message.')
print(plaintext)
input('Press enter to quit')

# This is for decoding
#determinant_of_key_matrix = int(round(np.linalg.det(key_matrix)))




#print(determinant_of_key_matrix)
#print(inverse_mod(determinant_of_key_matrix))