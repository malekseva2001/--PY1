money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
spend_increase = spend * (1+increase)
month = 0
money_capital -= spend
money_capital += salary
month += 1
while money_capital >= 0:
    money_capital -= spend_increase
    if money_capital >= 0:
        money_capital += salary
        spend_increase = spend_increase * (1 + increase)
        spend = spend_increase
        month += 1
     # TODO Оформить решение

print(month)
