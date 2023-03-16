from django.shortcuts import render
from .models import Portfolio
import random
import math
import time


# Create your views here.

start_capital = 100000.00
cash = 0
volatility = 0.2  # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120  # количество дней наблюдения


def prices(stock_price, bond_price):
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    stock_price *= 1.0 + monthly_return
    bond_price = round(bond_price + 6)
    return stock_price, bond_price


def breifcase(stock_num, bond_num, cash):
    # Блок оценки стоимости портфеля
    stock_case = round((stock_price * stock_num), 2)
    bond_case = round((bond_price * bond_num), 2)
    personal_case = round((stock_case + bond_case + cash), 2)
    stock_interest = round(stock_case / (personal_case / 100))
    bond_interest = 100 - stock_interest
    cash += 20000


# def upload(request):
#     if request.method == 'POST':
#         cash = 20000
#         return cash, render(request, 'main/index.html')





def index(request):
    item_1_title = Portfolio.objects.all()[0].title
    item_1_num = Portfolio.objects.all()[0].num
    item_1_price = Portfolio.objects.all()[0].price
    item_2_title = Portfolio.objects.all()[1].title
    item_2_num = Portfolio.objects.all()[1].num
    item_2_price = Portfolio.objects.all()[1].price

    item_1_sum = item_1_num * item_1_price
    item_2_sum = item_2_num * item_2_price
    capital = item_1_sum + item_2_sum

    return render(request, 'main/index.html', {'item1_title': item_1_title,
                                               'item1_num': item_1_num,
                                               'item1_sum': item_1_sum,
                                               'item1_price': item_1_price,
                                               'item2_title': item_2_title,
                                               'item2_num': item_2_num,
                                               'item2_sum': item_2_sum,
                                               'item2_price': item_2_price,
                                               'capital': capital,
                                               'cash': cash})


