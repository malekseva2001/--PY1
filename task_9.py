salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
money_capital = salary - spend
increase_spend = spend * (1 + increase)
need_money += (-money_capital)
for _ in range(1, months):
    money_capital = salary - increase_spend
    spend = increase_spend
    increase_spend = spend * (1 + increase)
    need_money += (-money_capital)

 # TODO Оформить решение

print(round(need_money))
