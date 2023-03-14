from django.shortcuts import render
from .models import Portfolio
# Create your views here.


stock_price = 100
bond_price = 1000

def sum_1(num, price):
    sum = num * price
    return sum


def index(request):
    item_1_title = Portfolio.objects.all()[0].title
    item_1_num = Portfolio.objects.all()[0].num
    item_1_sum = sum_1(item_1_num, stock_price)
    item_2_title = Portfolio.objects.all()[1].title
    item_2_num = Portfolio.objects.all()[1].num
    item_2_sum = sum_1(item_2_num, bond_price)
    return render(request, 'main/index.html', {'item1_title': item_1_title,
                                               'item1_num': item_1_num,
                                               'item1_sum': item_1_sum,
                                               'stock_price': stock_price,
                                               'item2_title': item_2_title,
                                               'item2_num': item_2_num,
                                               'item2_sum': item_2_sum,
                                               'bond_price': bond_price})


