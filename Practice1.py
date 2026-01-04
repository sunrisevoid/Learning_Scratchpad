#boolean learning

# name = input('Your Name: ')
# if name == 'Mary':
#     print('Hello Mary')
# else:
#     print('Wrong name')   
#     quit()
# password = input('Your Password: ')
# if password == 'swordfish':
#     print('Access granted.')
# else:
#     print('Wrong password')
#     quit()

# name = input('Your Name: ')
# if name == 'Alice':
#     print('Hi, Alice.')
# else:
#     print('I have no use for you.')
#     quit()
# 
# uage = input('Your age: ')
# age = int(uage)
# if age == 12:
#     print('You are surely Alice.')
# elif age > 12 and age < 100:
#     print('You are not Alice, kiddo.')
# elif age > 100 and age < 2000:
#     print('You are not Alice, grannie.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')
# else:
#     print('You are not Alice.')
# quit()

# spam = 1
# while spam < 20:
#     print('H' + ('e' * spam) + 'llo, w' + ('o' * spam) + 'rld' + ('!' * spam))
#     spam = spam + 1

# name = ''
# hint = 'That is not your name. '
# hp = 0
# while name != 'your name':
#     print((hint * hp) + 'Please type your name.')
#     name = input()
#     hp = 1
# print('Thank you!')

# hint = ''
# while True:
#     print(hint + 'Please type your name.')
#     if input() == 'your name':
#         break
#     hint = 'That is not your name. '
# print('Thank you!')

# hint = ''
# while input(hint + 'Please type your name: ') != 'your name':
# 	hint = 'That is not your name. '
# print('Thank you!')

# while True:
# 	print('Who are you?')
# 	name = input()
# 	if name != 'Joe':
# 		continue
# 	print('Hello, Joe. What is the password? (It is a fish.)')
# 	password = input()
# 	if password == 'swordfish':
# 		break
# print('Access granted.')

# name = ''
# while not name:
# 	print('Enter your name:')
# 	name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
# 	print('Be sure to have enough room for all your guests.')
# print('Done')

# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)




