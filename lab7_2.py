n = int(input("Введіть кількість слів: "))

result = []

for i in range(n):
    word = input("Введіть слово: ")

    new_word = " ".join(word)

    result.append(new_word)

final_string = ",".join(result)

print("Результат:", final_string)
