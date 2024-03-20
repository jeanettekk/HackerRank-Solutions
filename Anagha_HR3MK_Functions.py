# Week 1:

# Ratios of positives , negatives and zero values in an array

def plusMinus(arr):
    zeros = 0
    negatives = 0
    positives = 0
    for value in arr:
        if value == 0:
            zeros += 1
        elif value > 0:
            positives += 1
        else:
            negatives += 1
    total = zeros + positives + negatives
    zeros /= total
    positives /= total
    negatives /= total
    print(f"{positives:.6f}\n{negatives:.6f}\n{zeros:.6f}")
  

# Keeping track of maximum and minimum score records

def breakingRecords(scores):
    n = len(scores)
    max_count = 0
    min_count = 0
    current_min = scores[0]
    current_max = scores[0]
    for i in range(n):
        if scores[i] > current_max:
            max_count += 1
            current_max = scores[i]
        if scores[i] < current_min:
            min_count += 1
            current_min = scores[i]
    return [max_count, min_count]


# Convert to and fro into accepted camelCase format for class, method and variable

def toCamelCase(input_list):
    for j in range(len(input_list)):
        s = input_list[j]

        if s[0] == 'S':
            if s[2] == 'M':
                # essentially the same but one works one doesn't.
                # s = s[:-2]
                s = s.replace('()' , '')
            s = s[4:]
            for i in range(len(s)):
                if s[i].isupper():
                    if i != 0:
                        s = s[:i] + ' ' + s[i].lower() + s[i + 1:]
                    else:
                        s = s[i].lower() + s[i + 1:]

        if s[0] == 'C':
            s_list = s[4:].split()
            result = ''.join(map(str.capitalize, s_list[1:]))
            if s[2] == 'C':
                s = s_list[0].capitalize() + result
            elif s[2] == 'M':
                s = s_list[0] + result + '()'
            else:
                s = s_list[0] + result

        print(s)


# Find divisible sum pairs in given array

def divisibleSumPairs(n, k, ar):
    pairs_count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                pairs_count += 1
    return pairs_count


# Mock Sample: FizzBuzz
# return values depend on whether numbers in given range are divisible by 3 or 5 or both or neither

def fizzbuzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        if (i % 3 == 0) and (i % 5 != 0):
            print("Fizz")
        if (i % 3 != 0) and (i % 5 == 0):
            print("Buzz")
        else:
            print(i)


# Week 2:

# grading student: rounding off by adding one or two marks to students who have scored over 38 marks.

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        difference = 5 - (grade % 5)
        if difference < 3 and grade >= 38:
            grade += difference
        new_grades.append(grade)
    return new_grades
    

# flipping the bits of a decimal number

def flippingBits(num):
    return (1 << 32) - 1 - num


# finding difference of number sums representing each diagonal of given matrix

def diagonalDifference(arr):
    sq_length = len(arr[0])
    dia_1 = [] * sq_length
    dia_2 = [] * sq_length
    for i in range(0, sq_length):
        for j in range(0, sq_length):
            if i == j:
                dia_1.append(arr[i][j])
            if i+j == sq_length-1:
                dia_2.append(arr[i][j])
    sum1 = sum(dia_1)
    sum2 = sum(dia_2)
    return sum2-sum1 if sum2 > sum1 else sum1-sum2


# Count valleys traversed through path represented by characters D and U (Down and Up)

def countingValleys(path):

    altitude = 0
    num_valley = 0
    below_sea = False

    for step in path:
        if step == 'U':
            altitude += 1
        if step == 'D':
            altitude -= 1
        if altitude < 0:
            below_sea = True
        if altitude == 0 and below_sea:
            num_valley += 1
            below_sea = False
    return num_valley
