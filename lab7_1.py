text = input("Введіть рядок: ")

letters = 0
digits = 0

for symbol in text:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        digits += 1

print("Кількість літер:", letters)
print("Кількість цифр:", digits)
