# TODO решите задачу
import json  # Импортируем модуль для работы с JSON
def task() -> float:
    """
       Функция считывает JSON файл, вычисляет сумму произведений значений ключей "score" и "weight" в каждом словаре
       и возвращает результат, округленный до 3 знаков после запятой.
       """
    # Чтение JSON данных из файла input.json:
    with open("input.json", "r") as file:
        data = json.load(file) # Считываем JSON данные и преобразуем их в список словарей

    total_sum = 0.0 # Инициализируем переменную для накопления суммы произведений

    # Проходим по каждому словарю в списке
    for item in data:
        # Извлекаем значения по ключам "score" и "weight"
        score = item.get("score", 0) # Значение по ключу "score", если ключа нет, используем 0
        weight = item.get("weight", 0) # Значение по ключу "weight", если ключа нет, используем 0
        # Вычисляем произведение и добавляем его к общей сумме
        total_sum += score * weight
    # Округляем результат до 3 знаков после запятой
    return round(total_sum, 3)
# Вызываем функцию и выводим результат
if __name__ == "__main__":
    print(task())