####### Problem Statement #######
# You have been given an array containg numbers.
# Find and return the largest sum in a contiguous subarray within the input array.

# Example 1:
# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.

# Example 2:
# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    sumArray = sum(arr)
    maxSum = sumArray
    while len(arr) > 1:
        if arr[0] > arr[len(arr)-1]:
            arr = arr[:-1]
        else:
            arr = arr[1:]
        if sum(arr) > maxSum:
            maxSum = sum(arr)
    return maxSum

    # def max_sum_subarray(arr):
    # max_sum = arr[0]
    # current_sum = arr[0]

    # print("BEFORE IT ALL BEGINS | Array is {}, max_sum is {}, current_sum is {}". format(arr, max_sum, current_sum))

    # for num in arr[1:]:
    #     current_sum = max(current_sum + num, num)
    #     max_sum = max(current_sum, max_sum)
    #     print("num is {}, max_sum is {}, current_sum is {}". format(num, max_sum, current_sum))
    # return max_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)

arr = [-1,100,-80]
solution = 100  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)