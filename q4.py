#GIven three coordinate points A, B and C, find the missing point D such that ABCD is a parallelogram.
#if there are multiple solutions,find the lexicographically samllest coordinate.


A = list(map(int, input("Enter the coordinates of A: ").split()))
B = list(map(int, input("Enter the coordinates of B: ").split()))
C = list(map(int, input("Enter the coordinates of C: ").split()))

D = [0,0]

a1 = A[0] + C[0] - B[0]
a2 = A[0] + B[0] - C[0]
a3 = B[0] + C[0] - A[0]

D[0] = min(a1,a2,a3)

b1 = A[1] + C[1] - B[1]
b2 = A[1] + B[1] - C[1]
b3 = B[1] + C[1] - A[1]

D[1] = min(b1,b2,b3)


print("Lexicographically smallest coordinates of D: ", D)
print("Other coordinates of D: ", a1,b1)
print("Other coordinates of D: ", a2,b2)
print("Other coordinates of D: ", a3,b3)
