from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.db.models import FieldDoesNotExist
from django.urls import reverse
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):

    """ Room Detail Definition """

    model = models.Room
