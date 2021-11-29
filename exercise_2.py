deposit = float(input("Введите сумму депозита: "))
end_deposit = float(input("Какую сумму вы хотите получить в конце: "))
percent = float(input("Под какой годовой процент(в десятичных дробях):"))
month = 0

x = ((percent / 12) * deposit)
x += deposit

while x < end_deposit:
    x += ((percent / 12) * x)
    month += 1
    print(month)