from django.shortcuts import render
from .models import Portfolio
import random
import math

# Create your views here.
start_capital = 100000.00
cash = 0

volatility = 0.2  # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120  # количество дней наблюдения


# Блок по расчету новой цены акции и облигации
def prices(stock_price, bond_price):
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    stock_price *= 1.0 + monthly_return
    bond_price = round(bond_price + 6)
    return stock_price, bond_price


# Блок оценки стоимости портфеля
def briefcase(stock_num, bond_num, cash, stock_price, bond_price):
    stock_case = round(stock_price * stock_num)
    bond_case = round(bond_price * bond_num)
    personal_case = round(stock_case + bond_case + cash)
    stock_interest = round(stock_case / (personal_case / 100))
    bond_interest = 100 - stock_interest
    cash += 20000
    return stock_case, bond_case, personal_case, stock_interest, bond_interest


def index(request):
    stocks = Portfolio.objects.all()[0]
    bonds = Portfolio.objects.all()[1]

    stock_price, bond_price = prices(stocks.price, bonds.price)

    stocks.price = round(stock_price)
    stocks.save()
    bonds.price = round(bond_price)
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
