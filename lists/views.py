from django.shortcuts import render
from .models import Item
from django.http import HttpResponse


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else: item_text = ''

    return render(request, 'home.html', {
        'new_item_text': item_text,
    })

