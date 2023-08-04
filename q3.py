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

def num_molecules(c_atoms, h_atoms, o_atoms):
    water_molecules = h_atoms // 2
    co2_molecules = c_atoms
    glucose_molecules = c_atoms // 6
    total_molecules = water_molecules + co2_molecules + glucose_molecules
    return total_molecules




arr = list(map(int, input("Enter no of c h and o: ").split()))

print(num_molecules(arr[0], arr[1], arr[2]))