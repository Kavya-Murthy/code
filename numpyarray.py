import numpy

sampleArray = numpy.array(
    [
        [3, 6, 9, 22],
        [16, 19, 20, 26],
        [27, 30, 32, 35],
        [37, 22, 44, 47],
        [52, 54, 55, 66],
    ]
)
print("Printing Input Array")
print(sampleArray)

print("\n Printing array of odd rows and even columns")
newArray = sampleArray[::2, 1::2]
print(newArray)