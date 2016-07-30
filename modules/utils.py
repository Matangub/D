
def maxValidate(numberList):
    previousNumber = numberList[0]
    for item in numberList:
        if(previousNumber > item or item == -1 ):
            return False

        previousNumber = item

    return True

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1
