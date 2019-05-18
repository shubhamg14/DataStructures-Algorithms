def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


def plus_one_one_line(A):
    s = ''.join(map(str,A))
    s = int(s) + 1
    return s


print(plus_one([9,9,9]))
print(plus_one([1,4,9]))
print(plus_one_one_line([9,9,9]))
print(plus_one_one_line([1,4,9]))
