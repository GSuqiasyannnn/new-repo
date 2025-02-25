#EX_1
#____________________________________________
# List_1 = []
# for i in range(1, 6):
#     List_1.append(i)
# print(List_1)
# List_1.sort()
# print(List_1)
# List_1.remove(1)
# List_1.pop()
# print(List_1)
#______________________________________________

#EX_2
# import random
# NAMES = ["David", "Karen", "Artaky", "Vzgon", "Pushkiny", "Arto-Tunj Boajyany"]
# Random = random.randint(0,len(NAMES) -1)
# WHO = NAMES[Random]
# print(f"The bill will pay {WHO}")
# ________________________________________________

#EX_4
# import random
# a = input('type your choice: 1 for rock, 2 for paper, 3 for scissors ')
# b = ['rock', 'paper', 'scissors']
# a = b[int(a) - 1]
# print(f"Your choise is {a}")
# c = random.choice(b)
# print('robot choice: ', c)
# if a == 'rock' and c == 'scissors' or a == 'paper' and c == 'rock' or a == 'scissors' and c == 'paper':
#     print("You Woonnn!!, congrats")
# elif a == 'rock' and c == 'paper' or a == 'paper' and c == 'scissors' or a == 'scissors' and c == 'rock':
#     print("You lose")
# else:
#     print('Again, Robot chose that what chose you ')
