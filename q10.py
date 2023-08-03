#Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.


def subArraySum(arr, n, sum):
    count = 0
    cum_sum = 0
    sum_dict = {}
    for i in range(n):
        cum_sum += arr[i]
        if cum_sum == sum:
            count += 1
        if (cum_sum - sum) in sum_dict:
            count += sum_dict[cum_sum - sum]
        if cum_sum in sum_dict:
            sum_dict[cum_sum] += 1
        else:
            sum_dict[cum_sum] = 1
    return count





if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    n = len(arr)
    k = int(input("Enter the no to be checked: "))
    print("Count of subarrays is ", subArraySum(arr, n, k))