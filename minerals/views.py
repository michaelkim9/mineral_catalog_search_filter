from django.shortcuts import render, get_object_or_404
from .models import Mineral
import random


def mineral_detail(request, pk):
    '''Detail view for mineral by primary key (pk)'''
    mineral = get_object_or_404(Mineral, pk=pk)
    random_mineral = random.choice(Mineral.objects.all())
    return render(
        request,
        'minerals/mineral_detail.html',
        {'mineral': mineral, 'random_mineral': random_mineral}
        )
