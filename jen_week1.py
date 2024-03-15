# CAMEL CASE 4
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input_string = sys.stdin.read()
list_input = input_string.splitlines()

for index, line in enumerate(list_input):

    if 'S' == line[0:1]:

        no_parenthesis = line.replace('()', '')
        new_line = no_parenthesis[4:]
        new_list = []

        for letter in new_line:

            if letter == letter.upper():

                new_list += ' '
                new_list += letter

            else:
                new_list += letter

        list_input[index] = ''.join(new_list).lower().strip()

    else:
        if 'M' == line[2:3]:

            line = line[4:]
            words_list = line.split()

            for index_two, word in enumerate(words_list):

                if index_two > 0:
                    words_list[index_two] = word.capitalize()

            list_input[index] = ''.join(words_list) + '()'.strip()

        elif 'V' == line[2:3]:

            line = line[4:]
            words_list = line.split()

            for index_two, word in enumerate(words_list):

                if index_two > 0:
                    words_list[index_two] = word.capitalize()

            list_input[index] = ''.join(words_list).strip()

        else:

            line = line[4:]
            words_list = line.split()
            new_list = []

            for word in words_list:
                new_list += word.capitalize().strip()

            new_line = ''.join(new_list)
            list_input[index] = new_line

for line in list_input:
    print(line)

# DIVISIBLE SUM PAIRS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def divisibleSumPairs(n, k, ar):
    original = ar
    new_list = []
    counter = 0

    for i in range(0, n):

        for j in range(0, n):

            if i >= j:
                continue

            else:

                if (ar[i] + ar[j]) % k == 0:
                    new_list += ar[i], ar[j]

    return round(len(new_list) / 2)

# SPARSE ARRAYS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def matchingStrings(strings, queries):

    start = 0,

    count = list(start * len(queries))

    for index, query in enumerate(queries):

        for string in strings:

            if query == string:

                count[index] += 1

    return count