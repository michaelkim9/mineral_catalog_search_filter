import random

from django.shortcuts import render
from django.db.models import Q


from minerals.models import Mineral

m = Mineral.objects.all()


def index(request):
    """Landing 'home' page view to display list of all mineral names"""
    minerals = m
    random_mineral = random.choice(m)

    return render(request,
                  'index.html',
                  {'minerals': minerals, 'random_mineral': random_mineral}
                  )


# Lists minerals for a selected letter search
def mineral_letter(request, letter):
    minerals = m.filter(name__istartswith=letter.lower())
    random_mineral = random.choice(m)

    return render(request, 'index.html', {'minerals': minerals,
                                          'active_letter': letter,
                                          'random_mineral': random_mineral})


# Text Search minerals by name and other mineral categories
def mineral_search(request):
    term = request.GET.get("q")
    minerals = m.filter(
       Q(name__icontains=term) |
       Q(group__icontains=term) |
       Q(image_caption__icontains=term) |
       Q(category__icontains=term) |
       Q(formula__icontains=term) |
       Q(crystal_system__icontains=term) |
       Q(color__icontains=term) |
       Q(luster__icontains=term) |
       Q(crystal_habit__icontains=term) |
       Q(specific_gravity__icontains=term) |
       Q(streak__icontains=term) |
       Q(strunz_classification__icontains=term)
    )
    random_mineral = random.choice(m)

    return render(request, 'index.html', {'minerals': minerals,
                                          'random_mineral': random_mineral})


# Search by mineral group
def mineral_group(request, group):
    random_mineral = random.choice(m)

    minerals = m.filter(group__icontains=group)
    return render(request, 'index.html', {'minerals': minerals,
                                          'random_mineral': random_mineral})


# Search by mineral color
def mineral_color(request, color):
    random_mineral = random.choice(m)

    minerals = m.filter(color__icontains=color)
    return render(request, 'index.html', {'minerals': minerals,
                                          'random_mineral': random_mineral})
