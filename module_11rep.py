import inspect

def introspection_info(obj):
    info = {}

    # Получаем тип объекта
    info['type'] = type(obj).__name__

    # Получаем атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    info['module'] = getattr(obj, '__module__', 'N/A')

    # Получаем другие свойства объекта 
    info['doc'] = getattr(obj, '__doc__', 'N/A')

    return info

# Пример использования
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2

# Создаем объект
my_obj = MyClass(10)

# Получаем информацию о объекте
obj_info = introspection_info(my_obj)
print(obj_info)

# Пример с числом
number_info = introspection_info(42)
print(number_info)



