def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num - 1)
        print("Valor final ->",num)
        return num
print(factorial(5))