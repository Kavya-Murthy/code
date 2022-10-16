import numpy

arrayOne = numpy.array([[4, 7, 9], [23 ,12, 20]])
arrayTwo = numpy.array([[52,35, 55], [41 ,73, 11]])

resultArray  = arrayOne + arrayTwo
print("addition of two arrays is \n")
print(resultArray)

for num in numpy.nditer(resultArray, op_flags = ['readwrite']):
   num[...] = num*num
print("\nResult array after calculating the square root of all elements\n")
print(resultArray)