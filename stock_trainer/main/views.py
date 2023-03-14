from django.shortcuts import render
from .models import Portfolio
# Create your views here.


def index(request):
    item_1_title = Portfolio.objects.all()[0].title
    item_1_num = Portfolio.objects.all()[0].num
    item_2_title = Portfolio.objects.all()[1].title
    item_2_num = Portfolio.objects.all()[1].num
    return render(request, 'main/index.html', {'item1': item_1_title,
                                               'item2': item_1_num,
                                               'item3': item_2_title,
                                               'item4': item_2_num})


