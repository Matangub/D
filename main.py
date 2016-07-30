from modules.analyze import Analyze

analyze = Analyze()

while True:
    print("")
    
    userInput = input("your response: ")
    analyze.pushText(userInput)

    analyze.analyze()
