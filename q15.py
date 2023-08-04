#Hop Game
# Dr felix kline, the maths teacher at gauss school introduces the following game to teach his students the problem solving skills.
#He places a series of hopping stones in a row. Each stone has a number on it. The students start at the first stone and must hop to the end of the row. The number on the stone tells the student how many stones forward they can hop from that stone. The student must hop over the stones, but is not allowed to land on the stone with the number 0. The students must find the shortest path to the end.
#For example, if the stones are 1, 2, 0, 4, 1, 0, 2, 3, 1, then the shortest path is 1, 2, 4, 3, 1.

# Write a program to find the shortest path to the end of the row of stones.


def hopGame(stones):
    n = len(stones)
    jumps = [0 for i in range(n)]
    if n == 0 or stones[0] == 0:
        return float('inf')
    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if i <= j + stones[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]


if __name__ == "__main__":
    stones = [3,0,4,2,3,1]
    print(hopGame(stones))