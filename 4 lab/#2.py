# TODO импортировать необходимые молули
import csv  # Импортируем модуль для работы с CSV файлами
import json  # Импортируем модуль для работы с JSON файлами

INPUT_FILENAME = "input.csv"  # Имя входного CSV файла
OUTPUT_FILENAME = "output.json" # Имя выходного JSON файла

def task() -> None:
    """
        Функция считывает содержимое CSV файла, преобразует его в JSON структуру
        и записывает результат в выходной JSON файл с отступами равными 4.
        """
    # Открываем CSV файл для чтения
    with open(INPUT_FILENAME) as csv_file:
        # Создаем объект reader для чтения CSV файла
        csv_reader = csv.DictReader(csv_file)
        # Преобразуем данные в список словарей
        data = [row for row in csv_reader]

        # Открываем JSON файл для записи
        with open(OUTPUT_FILENAME, "w") as json_file:
            # Сериализуем данные в JSON и записываем в файл с отступами равными 4
            json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()
    # Читаем и выводим содержимое JSON файла для проверки
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
