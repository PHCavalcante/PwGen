import random

numbers = "1234567"
chars = "abcdefghijklmnopqrstuvwxyz"
upper = chars.upper()
special_chars = "!@#$%&*_?|"
allchars = chars + upper + numbers + special_chars

# print(random.choices(chars,  k = 1))
# print(random.choice(chars)) <- melhor até agora

password = ""
for i in range(20):
    password += random.choice(allchars)

print(password)
