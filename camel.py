camelcase = input("camelcase: ")
snake = ""

for letter in camelcase:
    if letter.isupper():
        snake += "_"
        snake += letter.lower()

    else:
        snake += letter

print(snake, end="")
