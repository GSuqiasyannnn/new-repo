#EX_1
#______________________________________
# word = "Python"
# for i in word:
#     print(i[-1:], sep= ' ')
#_________________________________________
# integers = [1, 2, 3, 4, 5, 6]
# for i in integers:
#     print(f"The {i} Index is {integers.index(i, 0, 6)}")
#___________________________________________
# Names = ["erexen", "Mec erexen", "Hin Erexen", "Papan", "Papy"]
# Age = [1, 12, 25, 56, 78]
# for name, age in zip(Names, Age):
#     print(f"Name is {name}, Age {age} old", sep= ' ')


#EX_2
# # ______________________________
# count = 0
# STUD = [172, 165, 192, 180, 181, 123, 143]
# for i in STUD:
#     count += i
#     result = count / 7
#
# print(f"Number of students = {len(STUD)}")
# print(f"Your total height is = {count}")
# print(f"Your full weight is = {result}")

#Ex-3
#_______________________________________

# X = int(input("Enter a number between 0 and 1000: "))
# if X < 0 or X > 1000:
#     print("Please enter a number between 0 and 1000.")
# else:
#     total_sum = 0
#
#     for i in range(2, X + 1, 2):
#         total_sum += i
#
#     print(total_sum)
#__________________________________________
#EX_4
# #-----------------------------------------
# Fizz_l = []
# Buzz_l = []
# FizzBuzz = []
# Game = int(input("Pls write your integer = "))
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         if Game == i:
#             FizzBuzz.append(i)
#         print("Your int is the list FizzBuzz", end=' ')
#     elif i % 3 == 0:
#         if Game == i:
#             print("Your int is the list Fizz", end = ' ')
#         Fizz_l.append(i)
#     elif i % 5 == 0:
#         if Game == i:
#             print("Your int is the list Buzz", end = ' ')
#         Buzz_l.append(i)
# print(Game)
# print(f"List of Fizz = {Fizz_l}")
# print(f"List of Buzz = {Buzz_l}")
# print(f"List of FizzBuzz = {FizzBuzz}")


#____________________________________________________
#EX_5