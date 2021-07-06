# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr
print(biggie_size([-1,3,5,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(arr):
    count = 0
    for val in arr:
        if val > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(arr):
    sum = 0
    for val in arr:
        sum += val 
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for val in list:
        sum += val 
    return sum/len(list)
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(arr):
    return len(arr)
print(length([10,20,30,40]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(arr):
    if len(arr) <= 1:
        return False
    min = arr[0]
    for val in arr:
        if val < min:
            min = val
    return min
print(minimum([55,44,22,77]))
print(minimum([1]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(arr):
    if len(arr) <= 1:
        return False
    max = arr[0]
    for val in arr:
        if val > max:
            max = val 
    return max
print(maximum([55,44,22,77]))
print(maximum([1]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(arr):
    myDictionary = {'sumTotal': 0, 'average': 0, 'minimum': arr[0], 'maximum': arr[0], 'length': len(arr)}
    for val in arr:
        if myDictionary['minimum'] < val:
            myDictionary['minimum'] = val
        if myDictionary['maximum'] > val:
            myDictionary['maximum'] = val
        myDictionary['sumTotal'] += val
        myDictionary['average'] = myDictionary['sumTotal'] / len(arr)
    return myDictionary
print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(arr):
    for i in range(0, (len(arr)-1)):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
print(reverse_list([37,2,1,-9]))