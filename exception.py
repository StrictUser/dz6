numOne = input("Enter some number ")
numTwo = input("Enter some number ")

try:
    numOne = int(numOne)
    numTwo = int(numTwo)
    print(numOne + numTwo)
except ValueError:
    numOne = str(numOne)
    numTwo = str(numTwo)
    print(numOne + numTwo)