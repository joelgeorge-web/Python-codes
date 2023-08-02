#Givem an array num of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times.
#You may assume that the majority element always exists in the array.

arr = list(map(int, input("Enter the array: ").split()))
n = len(arr)
count = 0
element = 0
for i in arr:
    if(arr.count(i)>count) and (arr.count(i)>n//2):
        count = arr.count(i)
        element = i
print(element)