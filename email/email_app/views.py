from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import User


class CreateViewUser(CreateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('success')


class ViewSuccess(View):

    def get(self, request):
        return render(request, 'page_success.html')
