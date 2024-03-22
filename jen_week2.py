def lonelyinteger(a):
    copy = a
    same = []

    for index, number in enumerate(a):

        for index2, number2 in enumerate(copy):

            if index != index2:

                if number == number2:
                    same.append(number)

    unique_num = list(set(a) - set(same))

    return unique_num[0]

# GRADING STUDENTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def gradingStudents(grades):

    for index, grade in enumerate(grades):

        if grade >= 38:
            new = round(grade)

            while new % 5 != 0:

                new += 1

            if (new - grade) < 3:

                grades[index] = new

    return grades

# FLIPPING BITS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def flippingBits(n):
    num_list = str(n).strip().split('\n')
    flipped_integers = []

    for numbers in num_list:

        binary = format(int(numbers), '#034b')
        binary_32 = binary[2:]
        flip = []

        for single_num in binary_32:

            if single_num == '0':

                flip.append('1')

            elif single_num == '1':

                flip.append('0')

        flip = ''.join(flip)
        flipped_integer = int(flip, 2)
        flipped_integers.append(flipped_integer)

    return flipped_integer

# DIAGONAL DIFFERENCE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def diagonalDifference(arr):
    items = len(arr)
    left_right = 0
    right_left = 0
    reverse_list = list(range(items))
    reverse_list.reverse()

    for number in range(items):

        left_right += arr[number][number]

        right_left += arr[number][reverse_list[number]]

    return abs(left_right - right_left)

# COUNTING SORT 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def countingSort(arr):

    counter = list((0,) * 100)

    for number in arr:
        counter[number] += 1

    return counter

# COUNTING VALLEYS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def countingValleys(steps, path):
    sea_level = 0
    valley_count = 0

    for letter in path:

        if letter == 'D':

            sea_level -= 1

        elif letter == 'U':

            sea_level += 1

            if sea_level == 0:
                valley_count += 1

    return valley_count

# PANGRAMS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from string import ascii_lowercase

def pangrams(s):
    alpha = list(ascii_lowercase)
    counter = list((0,) * len(alpha))
    pangram = True
    s = ''.join(s.split()).lower()

    for index, character in enumerate(s):

        if character in alpha:
            counter[alpha.index(character)] += 1

    for num in counter:

        if num == 0:
            pangram = False

    if pangram:
        return 'pangram'
    else:
        return 'not pangram'

# MARS EXPLORATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def marsExploration(s):
    items = len(s)
    sos = 'S', 'O', 'S',
    correct_list = list(sos * round(items / 3))
    count = 0

    for index, letter in enumerate(s):

        if letter != correct_list[index]:
            count += 1

    return count
