import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


def print_file_content(file_name):
    print(f"\n{file_name} - название файла:")
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")


def run_and_measure(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return end_time - start_time


def run_functions():
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")


def run_threads():
    threads = [
        threading.Thread(target=write_words, args=(10, "example5.txt")),
        threading.Thread(target=write_words, args=(30, "example6.txt")),
        threading.Thread(target=write_words, args=(200, "example7.txt")),
        threading.Thread(target=write_words, args=(100, "example8.txt"))
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# Выполнение функций
func_time = run_and_measure(run_functions)

# Вывод времени выполнения функций
print(f"Работа функций {func_time:.6f} секунд")

# Выполнение потоков
thread_time = run_and_measure(run_threads)

# Вывод времени выполнения потоков
print(f"Работа потоков {thread_time:.6f} секунд")

# Вывод содержимого файлов
for i in range(1, 9):
    print_file_content(f"example{i}.txt")
