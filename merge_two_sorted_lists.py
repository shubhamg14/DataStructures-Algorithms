def merge_two_sorted_lists(A,B):

    if len(A) == 0 and len(B) == 0:
        return
    elif len(A) == 0:
        return B
    elif len(B) == 0:
        return A

    C = []
    i = 0
    j = 0
    while i<len(A) and j<len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1

        else:
            C.append(B[j])
            j+=1


    if len(A)-i!=0:
        for k in range(i, len(A)):
            C.append(A[k])

    else:
        for k in range(j,len(B)):
            C.append(B[k])
        
    print(C)

merge_two_sorted_lists([1,5,8,10],[2,3,6,7,9])
