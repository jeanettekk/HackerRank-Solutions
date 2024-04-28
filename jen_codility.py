# TASK 4
def solution(N):
    if N == 0:
        return 50

    n_list = list(str(N))

    # If positive
    if N > 0:
        for index, number in enumerate(n_list):
            if int(number) < 5:
                n_list.insert(index, '5')
                return int(''.join(n_list))

        return int(''.join(n_list) + '5')
    # If negative
    else:
        for index, number in enumerate(n_list):
            if index != 0:
                if int(number) > 5:
                    n_list.insert(index, '5')
                    return int(''.join(n_list))

        return int(''.join(n_list) + '5')
