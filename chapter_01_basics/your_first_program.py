# This program says hello and asks for my name.add()

print('Hello, World!')
print('What is your name?') # Ask for their name
my_name = input('>')
print('It is good to meet you, ' + my_name)
print()
print('The length of your name is: ')
print(len(my_name))
print()
print('What is your age?') # Ask for their age
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
print()