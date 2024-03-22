def twoArrays(k, A, B):
    yes = 0
    A.sort()
    B.sort()

    for num_a in A:

        for num_b in B:

            if num_a + num_b >= k:
                yes += 1
                B.remove(num_b)
                break

    if n == yes:

        return 'YES'

    else:

        return 'NO'
