text = str(input("What Would You Like Translated?: ")).split()
for word in text:
    print(word[1:] + word[0] + "ay", end = " ")

print()
