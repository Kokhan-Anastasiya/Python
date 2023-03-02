# Task1: Напишите и запустите программу. которая выводит строку  "Hello world!"
print("Hello, world!")

#Task2: Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!
user_name = input("Please, enter user name: ")
print(f"Hello, {user_name}!")

#Task3: Напишите программу, которая на входе получает 2 числа, производит с ними арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.
x = int(input("Please, enter any number: "))
y = int(input("Please, enter any number: "))
sum = (x+y)
print(f"Результат = {sum}")
# Variant 2:
print(f"Результат = {y+x}")

# Task4:Напишите программу, чтобы вывести:
#
# *********
# *       *
# *       *
# *********
# Variant 1:
print("*********\n*       *\n*       *\n*********")

# Variant 2:
print("*********", "*       *", "*       *", "*********", sep='\n', end='')

# Variant 3:
print("""
*********
*       *
*       *
*********
""")

print("")


