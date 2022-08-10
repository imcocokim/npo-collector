from django.shortcuts import render
from .models import NPO
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def npos_index(request):
  npos = NPO.objects.all()
  return render(request, 'npos/index.html', {'npos': npos})

def npos_detail(request, npo_id):
  npo = NPO.objects.get(id=npo_id)
  return render(request, 'npos/detail.html', { 'npo': npo })

class NPOCreate(CreateView):
  model = NPO
  fields = ['name', 'topic', 'description', 'website']
  success_url = '/npos/'

class NPOUpdate(UpdateView):
  model = NPO
  fields = ['topic', 'description', 'website']

class NPODelete(DeleteView):
  model = NPO
  success_url = '/npos/'