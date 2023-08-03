#Your task is to find the number of molecules in a cup of soda which contains distilled water, carbon dioxide, and glucose.
#you have a machine thats able to count the number of atoms of carbon, hydrogen, and oxygen in a given sample.
# water: H2O
#caron dioxide: CO2
#Glucose: C6H12O6

#Let g be glucose, x be carbon dioxide, and w be water.

#total no of c o and h is given by the equations
# 6g + x = c ----> eqn1
# 12g + 2w = h ----> eqn2
# 6g + 2x + w = o ----> eqn3

#From this we can find the value of g, x, and w.

# eqn1 gives us x = c - 6g
# eqn2 gives us w = (h - 12g)/2
# Substituting in eqn3 we get g = (2o -4c - 2h)/2

g = 0
x = 0
w = 0



arr = list(map(int, input("Enter no of c h and o: ").split()))
c = arr[0]
h = arr[1]
o = arr[2]
print(arr)
g = o + c - 2*h/2
x = c - 6*g
w = (h - 12*g)/2
if g < 0 or x < 0 or w < 0:
    print("invalid")
else:
    print("No of glucose molecules: ", g//6)
    print("No of carbon dioxide molecules: ", x//1)
    print("No of water molecules: ", w//2)