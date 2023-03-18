from django.shortcuts import render
from .models import Portfolio
import random
import math

# Create your views here.
start_capital = 100000.00
cash = 0

volatility = 0.2  # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120  # количество дней наблюдения


# Блок по установке к начальным настройкам
def start_training():
    stocks = Portfolio.objects.all()[0]
    bonds = Portfolio.objects.all()[1]
    stocks.title, stocks.num, stocks.price = 'Акция', 500, 100
    bonds.title, bonds.num, bonds.price = 'Облигация', 50, 994
    stocks.save()
    bonds.save()


# Блок по расчету новой цены акции и облигации
def prices(stock_price, bond_price):
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    stock_price *= 1.0 + monthly_return
    bond_price = round(bond_price + 6)
    return round(stock_price), round(bond_price)


# Блок оценки стоимости портфеля
def briefcase(stock_num, bond_num, cashes, stock_price, bond_price):
    stock_case = round(stock_price * stock_num)
    bond_case = round(bond_price * bond_num)
    personal_case = round(stock_case + bond_case + cashes)
    stock_interest = round(stock_case / (personal_case / 100))
    bond_interest = 100 - stock_interest
    cashes += 20000
    return stock_case, bond_case, personal_case, stock_interest, bond_interest


# Обновление в начале запуска
start_training()


def index(request):
    stocks = Portfolio.objects.all()[0]
    bonds = Portfolio.objects.all()[1]

    stocks.price, bonds.price = prices(stocks.price, bonds.price)

    stocks.save()
    bonds.save()

    item_1_sum = stocks.num * stocks.price
    item_2_sum = bonds.num * bonds.price
    capital = item_1_sum + item_2_sum

    data = {'item1_title': stocks.title,
            'item1_num': stocks.num,
            'item1_sum': item_1_sum,
            'item1_price': stocks.price,
            'item2_title': bonds.title,
            'item2_num': bonds.num,
            'item2_sum': item_2_sum,
            'item2_price': bonds.price,
            'capital': capital,
            'cash': cash}

    return render(request, 'main/index.html', context=data)
