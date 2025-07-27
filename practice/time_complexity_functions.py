def print_array_elements(arr):
    # O(n) - Linear time, iterates through each element once
    for i in range(len(arr)):
        print(arr[i])

def double_all_elements(arr):
    # O(n) - Linear time, iterates through each element once
    for i in range(len(arr)):
        arr[i] = arr[i] * 2

def double_first_element(arr):
    # O(1) - Constant time, operates on a single element
    if len(arr) > 0:
        arr[0] = arr[0] * 2

def create_multiplication_table(arr):
    # O(n^2) - Quadratic time, creates a table with n * n multiplications
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i] * arr[j])