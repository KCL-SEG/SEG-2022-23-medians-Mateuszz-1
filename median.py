"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median(numbersList):
    sortedList = numbersList.sort()
    listLength = len(numbersList)
    if (listLength % 2) == 0:
        number1 = numbersList[int(((listLength / 2) - 1))]
        number2 = numbersList[int((listLength / 2))]
        return (number1 + number2) / 2
    elif (listLength % 2) == 1:
        return numbersList[int(((listLength / 2) - 0.5))]


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        medianNumber = median(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(medianNumber)
