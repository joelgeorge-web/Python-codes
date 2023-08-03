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
print(arr)

#CO2 molecules only if h = 0
if arr[1] == 0 and arr[0] != 0:
    if 2*arr[0] == arr[2]:
        print("No of CO2 molecules: ",arr[0])
    else:
        print("invalid")
#H2O molecules
elif arr[0] == 0 and arr[1] != 0:
    if arr[1] == 2*arr[2]:
        print("H2O: ", arr[2])
    else:
        print("invalid")
elif arr[0] !=0 and arr[1] != 0 and arr[2] != 0:
    g = abs(2*arr[2] - 4*arr[0] - 2*arr[1])/2
    x = abs(arr[0] - 6*g)
    w = abs((arr[1] - 12*g)/2)
    if g < 0 and x < 0 and w < 0:
        print("invalid")
    else:
        print("No of glucose molecules: ", g)
        print("No of carbon dioxide molecules: ", x)
        print("No of water molecules: ", w)