# A supermarket maintains a pricing format for all its products. A value N is printed on each product. When the scanner reads the value N on the item, the product of all the digits in the value N is the price of the item. The task here is to design the software such that given the code of any item N the product (multiplication) of all the digits of value should be computed(price).

price = int(input("Enter the code of the item: "))

digits = [int(digit) for digit in str(price)]

product = 1

for i in range(len(digits)):
    if i == 0:
        product = digits[i]
    else:
        product *= digits[i]

print(product)
