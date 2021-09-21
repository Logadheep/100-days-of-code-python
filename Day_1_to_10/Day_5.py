# Computing no. Of capital letters, small letters
# digits, consonants, vowels, spaces.

#getting input
#constraint:
#     no special characters in input as well as
#     no escape sequences
string = input()

#initializing
upcase = 0
vowel = 0
lowcase = 0
consonants = 0
spaces = 0
digit = 0
#computational logic
for i in string:
    if i.isupper():
        upcase += 1
    elif i.islower():
        lowcase += 1
    elif i in 'aAeEiIouU':
        vowel += 1
    elif i not in 'aAeEiIouU':
        consonants += 1
    elif i == ' ':
        spaces += 1
    elif i.isdigit():
        digit += 1

print(f'There are {upcase} capital letters.')
print(f'There are {lowcase} small letters.')
print(f'There are {consonants} consonants.')
print(f'There are {vowel} vowels.')
print(f'There are {consonants} spaces.')
print(f'There are {digit} digits')

