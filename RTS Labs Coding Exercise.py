def aboveBelow(intList, compareNumber):
    if not checkIntList(intList):
        return False

    if not checkInt(compareNumber):
        return False
    
    above = sum(map(lambda x: x > compareNumber, intList))
    below = sum(map(lambda x: x < compareNumber, intList))
    results = {"above": above, "below": below}
    return results

def checkInt(number):
    #Checks if a variable is an integer
    if not isinstance(number, int):
        print("There is not an integer")
        return False
    return True
    

def checkIntList(intList):
    #Checks if a list has only integers and is not empty
    if not intList:
        print("List of integers is empty")
        return False
    results = (sum(map(lambda x:  not isinstance(x, int), intList)))
    if results > 0:
        print("List of integers is not in correct format")
        return False
    return True

def checkString(string):
    if not isinstance(string, str):
        print("String is not in correct format")
        return False
    if len(string) == 0:
        print("String is empty")
        return False
    return True

def stringRotation(string, numToRotate):
    if not checkString(string):
        return False
    if not checkInt(numToRotate):
        return False
    cutOff = len(string) - (numToRotate % len(string))
    return string[cutOff:] + string[:cutOff]
        

def main():
    aboveBelowResults = aboveBelow([1, -34, 8, 45, 7, 63], 7)
    if aboveBelowResults:
        print(aboveBelowResults)
    stringRotationResults = stringRotation("Sa5mth6Tue5dyyy", 20)
    if stringRotationResults:
        print(stringRotationResults)
    

main()
        
