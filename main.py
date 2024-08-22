def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n+1):
            if i + j == n or n % (i + j) == 0:
                result += str(i) + str(j)
    return result

# Проверка для всех чисел от 3 до 20
for num in range(3, 21):
    password = generate_password(num)
    print(f"{num} - {password}")

# Ввод пользователя
user_input = int(input("Введите число от 3 до 20: "))
if 3 <= user_input <= 20:
    print(f"Пароль для {user_input}: {generate_password(user_input)}")
else:
    print("Число должно быть от 3 до 20")


