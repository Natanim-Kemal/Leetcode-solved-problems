def recursive_sum(arr):
    count = 0 
    if arr.pop() == False:
        return count
    else:
        arr.pop()
        print(arr)
        count += recursive_sum(arr)
    return count


recursive_sum([1,1,2,4,5,6])
recursive_sum([1])
recursive_sum([])