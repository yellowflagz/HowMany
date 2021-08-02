import string
# Importing string library to generate a list of letters. Defining variables and lists.
numletters = 0
numdigits = 0
numsymbols =0
sentence_splice = []
alphabet = list(string.ascii_letters)
digits = list(string.digits)
# Ask for the sentence
print('Hi! Enter a sentence and I will tell you exactly how many letters and numbers it has :)')
sentence = str(input())
# With splice we add each letter/digit/symbol/space of the sentence into a list
sentence_splice[:] = sentence
# Iterating the spliced sentence, with a few counters and conditionals we get the number of each digit,
# word and symbol. We also ignored blank spaces.
for i in sentence_splice:
    if i in alphabet:
        numletters = numletters + 1
    elif i in digits:
        numdigits = numdigits+ 1
    elif i == '' or i == ' ':
        continue
    else:
        numsymbols = numsymbols+ 1
# Finally we can print the result!
print('Number of letters: ' + str(numletters))
print('Number of digits: ' + str(numdigits))
print('Number of symbols: ' + str(numsymbols))



