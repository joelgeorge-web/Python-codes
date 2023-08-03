#Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.


def subArraySum(arr, n, sum):
    count = 0
    i = 0
    while i < n:
        curr_sum = 0
        j = i
        while j < n:
            curr_sum += arr[j]
            if curr_sum == sum:
                count += 1
            j += 1
        i += 1
    return count




if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    n = len(arr)
    k = int(input("Enter the no to be checked: "))
    print("Count of subarrays is ", subArraySum(arr, n, k))