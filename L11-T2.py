def fibonacci(number):
    fibonacci_list = []
    for i in range(number):
        if i == 1 or i == 0:
            fibonacci_list.append(1)
        else:
            b = int(fibonacci_list.__getitem__(i-1)) + int(fibonacci_list.__getitem__(i-2))
            fibonacci_list.append(b)
    return (fibonacci_list.__getitem__(number-1))

userInput = int(input("Input the amount of months:\n"))
totalOfRabbit = int(fibonacci(userInput)) + int(fibonacci(userInput-1))
print("After "+str(userInput)+" months, there will be "+str(totalOfRabbit)+" rabbit couples.")