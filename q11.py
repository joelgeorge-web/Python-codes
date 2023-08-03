#Given n non negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


def trap(height):
    n = len(height)
    left = [0] * n
    right = [0] * n
    water = 0
    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])
    right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])
    for i in range(0, n):
        water += min(left[i], right[i]) - height[i]
    return water


if __name__ == "__main__":
    height = list(map(int, input("Enter the array: ").split()))
    print(trap(height))