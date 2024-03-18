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
