def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()


# Вызов test_function
print("Вызываем test_function:")
test_function()

# Попытка вызвать inner_function вне test_function
print("\nПытаемся вызвать inner_function вне test_function:")
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
    print("inner_function не доступна вне test_function")


