salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_needed = 0  # Общая сумма, необходимая для покрытия расходов
current_spend = spend  # Текущие расходы на месяц
for month in range(months):
        if month > 0:  # На втором месяце и далее расходы увеличиваются
            current_spend *= (1 + increase)

        # Вычисляем нехватку средств после зарплаты
        deficit = current_spend - salary
        if deficit > 0:
            total_needed += deficit
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_needed))
