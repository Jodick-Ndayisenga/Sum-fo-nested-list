class Sum:
    def __init__(self, wordList:list, target:int):
        self.wordList = wordList
        self.target = target

    def GetNumbers(self,List:list) ->list:
        firstNumber = List[0]
        otherNumber = 0
        secondValue = 0
        for i in List:
            if(firstNumber+i)==self.target:
                otherNumber+=i
                secondValue = i
                break
        return ([firstNumber+otherNumber,firstNumber, secondValue])

    def Control(self) ->list:
        original = self.wordList.copy()
        newArray = self.wordList
        i = 0
        while i< len(original):
            result = self.GetNumbers(newArray)
            if result[0] == self.target:
                firstIndex = original.index(result[1])
                secondIndex = original.index(result[2])
                break
            else:
                newArray = newArray[1:]
                i+=1

        return ([firstIndex, secondIndex])

firstAttempt = Sum([2,5,7,9,6,10], 10)
print(firstAttempt.Control())