number1=12
number2=210
numbers=[1,3,5,12,123,210,1345]
numberscount= len(numbers)
print(numberscount)
x=0

for number in numbers:
    if number2 == number:
        print(True)
        print(number)
        break
    else:
        print(False)
        print(number)

while x < len(numbers):
    if number2 ==numbers[x]:
        print(number2, "serinin", x+1, ".ci sirasinda bulunmustur")
        break
    else:
        x += 1
else:
    print("Girilen sayi listede bulunamadi.")