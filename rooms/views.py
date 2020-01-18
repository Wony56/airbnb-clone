from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models


def home(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
    except ValueError:
        return redirect("/")
    except EmptyPage and PageNotAnInteger:
        return redirect("/")

    return render(request, "rooms/home.html", {"page": rooms})

