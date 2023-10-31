import keyboard

file = open('age.txt', 'w')
print('This is age calculator !', file = file)

print ("This pogram is used to calculate age\n")

keyboard.press_and_release('enter')
a = int (input("Enter current year\t") or "2023")
keyboard.press_and_release('enter')

b = int (input("enter you birth year\t") or "1981")

if a == b:
    print ("same input")

a = int(a)
b =int (b)
#subtract the converted user input from the current year
age = a - b


print(age, file = file)
file.close()
print(age,"years")
print ("Results depends on your input")

file.close()
keyboard.press_and_release('enter')
input("Enter to exit")
keyboard.press_and_release('enter')
import os
p = path = ("age.txt")
os.system(path)
file = open ("age.txt")
