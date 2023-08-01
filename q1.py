#Given an array arr[] of N integers, In one step, any element of the array can either be increased or decreased by one.
#Find minimum steps required such that the product of the array elements becomes 1.

arr = list(map(int, input("Enter the array elements: ").split()))
n = len(arr)
count = 0
b = 0
for i in range(n):
    if arr[i] == 0:
        arr[i] = arr[1]+1
        count = count + 1
    elif arr[i] < 0 or arr[i] > 1:
        arr[i] = abs(arr[i])
        b = arr[i]-1
        arr[i] -= b
        count += b

print("min no of steps:", count)

