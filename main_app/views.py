from django.shortcuts import render, redirect
from .forms import WidgetForm
from .models import Widget
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.db.models import Sum
# Create your views here.

class WidgetList(ListView):
  model = Widget

def index(request):
  total = Widget.objects.aggregate(Sum('quantity'))
  widgets = Widget.objects.all()
  print(widgets)
  form = WidgetForm()
  return render(request, 'index.html',{'form':form, 'widgets': widgets, 'total': total})


def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('index')
 
class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'