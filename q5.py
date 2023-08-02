#Givem an array num of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
#You may assume that the majority element always exists in the array.

arr = list(map(int, input("Enter the array: ").split()))
n = len(arr)
count = 0

for i in range(n):
    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1
    if count > n/2:
        print(arr[i])
        break