word = input("Input: ")

new_word = ""

for letter in word:
    if letter.lower() not in "aeiou":
        new_word += letter
    else:
        pass

print(new_word, end="")
