#Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
#Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj.
#If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
#Your goal is to maximize the number of your content children and output the maximum number.


def cookie(g,s):
    g.sort()
    s.sort()
    i = 0
    j = 0
    count = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

testcases = int(input("Enter no of testcases: "))
while testcases:
    g = list(map(int, input("Enter greed factors: ").split()))
    s = list(map(int, input("Enter cookie sizes: ").split()))
    print(cookie(g,s))
    testcases -= 1