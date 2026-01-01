# This program says hello and asks for user's name and age

print('Hello World!')
print()
print('May I have your name?') #asks for user's name
print()
myName = input('Your response: ')
print()
print('It is great to meet you ' + myName + '!')
print()
print('You have ' + (str(len(myName))) + ' characters in your name!')
print()
print('What is your age?') #asks for user's name
print()
myAge = input('Your response: ')
print()
print('You will be ' + str(int(myAge) + 1) + ' in a year! WOWEE ZOWEE!')
print()
print('How do you feel about that?') #asks for user's feelings lmao
print()
dontCare = input('Your response: ')
print()
print('Haha! "' + dontCare + '"? What a dumb response! Haha!')
