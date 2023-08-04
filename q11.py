#Given n non negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


def trap(height): #this is the function to find the amount of water that can be trapped
    n = len(height) #this is the length of the height
    left = [0] * n #this creates a list of n elements with value 0
    right = [0] * n #this creates a list of n elements with value 0
    water = 0 #this is the amount of water that can be trapped initally
    left[0] = height[0] #this is the first element of the left list
    for i in range(1, n): #this is the range of the left list
        left[i] = max(left[i - 1], height[i]) #this is the max of the left list
    right[n - 1] = height[n - 1] #this is the first element of the right list
    for i in range(n - 2, -1, -1): #this is the range of the right list
        right[i] = max(right[i + 1], height[i]) #this is the max of the right list
    for i in range(0, n): #this is the range of the water
        water += min(left[i], right[i]) - height[i] #this is the amount of water that can be trapped
    return water #this returns the amount of water that can be trapped


if __name__ == "__main__":
    height = list(map(int, input("Enter the array: ").split()))
    print(trap(height))