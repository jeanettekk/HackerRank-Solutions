def flippingBits(n):
    num_list = str(n).strip().split('\n')

    for numbers in num_list:

        binary = str(bin(int(numbers)))
        binary_32 = str(binary.zfill(32))
        flip = []

        for single_num in binary_32:

            if single_num != 'b':

                if single_num == '0':

                    flip.append('1')

                elif single_num == '1':

                    flip.append('0')

        final = []

        for index, num_flip in enumerate(flip):

            max_index = 31

            if num_flip == '1':
                temp = max_index - index
                power = 2**temp
                final.append(power)

        return sum(final)
