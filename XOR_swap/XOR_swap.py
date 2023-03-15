a = 2897124901
b = 35890124446

print("a START:", a)
print("b START:", b)

a = a ^ b #assign the first bitwise XOR to a
print("\na after a = a ^ b:", a)

b = a ^ b #assign the second bitwise XOR to b
print("\nb after b = a ^ b:", b)

a = a ^ b #assign the third bitwise XOR to a
print("\na after XOR swap:", a)
print("b after XOR swap:", b)
#after 3 direct bitwise XOR's in this fashion the variables will have swapped values
#(without a third variable!)
