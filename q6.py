#Your friend, Alice, is starting a dog walking business. She already has K dog walkers employed, and today there are N dogs that need to be walked.
#Each dog walker can walk multiple dogs at the same time, so the dogs will be arranged into K nonempty groups, and each group will then be walked by a single dog walker.
#However, smaller dogs can be aggressive towards larger dogs, and that makes it harder to walk them together.
#More formally, if the smallest dog in a group has size a, and the largest dog in the group has size b, then the range of the group is defined as b-a.
#In particular, the range of a group consisting of a single dog is 0. The smaller the range of a group is, the easier it is to walk that particular group. 
#Hence Alice would like to distribute the dogs among the dog walkers so that the sum of ranges of the groups is minimized. Also, since she doesn’t want any of the dog walkers to feel left out, she makes sure each dog walker gets to walk at least one dog.
# Given N, K and the sizes of the dogs, can you help Alice determine what is the minimum sum of ranges over the K groups if the dogs are arranged optimally?
#https://medium.com/xtremefun/xtreme-10-0-walking-dogs-4bd783e4b114


arr = list(map(int, input("Enter no of dogs and dog walkers: ").split()))
N = arr[0]
K = arr[1]
diff = []
rang = 0
dogs = list(map(int, input("Enter sizes of dogs: ").split()))
def dog(N,K,dogs):
    n = len(dogs)
    dogs.sort()
    range1 = dogs[n-1] - dogs[0] #range if all dogs are walked by one person
    for i in range(n-1):
        a = dogs[i+1]-dogs[i]
        diff.append(a)
    diff.sort(reverse=True)
    print(diff)
    rang = range1 - sum(diff[0:K-1])
    
    return rang

print(dog(N,K,dogs))


