numbers = [5, 20, 30, 35, 50]
inputNumber = int(input("Enter a number"))
for i in range(len(numbers)):
    if inputNumber <= numbers[i]:
        numbers.insert(i, inputNumber)
        break
    if i == len(numbers) - 1:
        numbers.append(inputNumber)
print(numbers)