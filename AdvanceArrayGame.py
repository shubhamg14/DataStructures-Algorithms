def advanced_array_game(A):
    last_index = len(A) - 1
    index = 0
    max_index = 0

    while max_index < last_index and index <= max_index:
        max_index = max(max_index,A[index]+index)
        index+=1

    return index <= max_index

print(advanced_array_game([3,2,0,0,2,0,1]))