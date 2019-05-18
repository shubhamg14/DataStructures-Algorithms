#Time Complexity : O(n^2)
#Space Complexity : O(1)
def brute_force_sum(A,target_value):
    for i in range(0,len(A)):
        for j in range(1,len(A)):
            if A[i]+A[j] == target_value:
                print(A[i] , " ", A[j])
                return
    return print("Not Found")

#Time Complexity : O(n)
#Space Complexity : O(n)
def hash_table_sum(A,target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            return print (ht[A[i]],A[i])
        else:
            ht[target-A[i]]=A[i]
    return False

#Time Complexity : O(n)
#Space Complexity : O(1)
def inc_dec_two_sum(A,target):
    i = 0
    j = len(A)-1
    while i<j:
        if A[i]+A[j] == target:
            return print(A[i],A[j])
        elif A[i]+A[j]>target:
            j -= 1
        else:
            i += 1
    return print("Not Found")

brute_force_sum([-2,1,2,4,7,11],13)
hash_table_sum([-2,1,2,4,7,11],13)
inc_dec_two_sum([-2,1,2,4,7,12],13)