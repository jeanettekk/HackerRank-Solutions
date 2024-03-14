strings1 = ['ab', 'ab', 'abc']
queries1 = ['ab', 'abc', 'bc']


def matchingStrings(strings, queries):

    start = 0,

    count = list(start * len(queries))

    for index, query in enumerate(queries):

        for string in strings:

            if query == string:

                count[index] += 1

    return count


if __name__ == '__main__':

    result = matchingStrings(strings1, queries1)

    print(result)
