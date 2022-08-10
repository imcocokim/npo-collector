from django.shortcuts import render,redirect
from .models import NPO
from .forms import EventForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def npos_index(request):
  npos = NPO.objects.all()
  return render(request, 'npos/index.html', {'npos': npos})

def npos_detail(request, npo_id):
  npo = NPO.objects.get(id=npo_id)
  event_form = EventForm()
  return render(request, 'npos/detail.html', { 'npo': npo, 'event_form': event_form })

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

def add_event(request, npo_id):
  form = EventForm(request.POST)
  if form.is_valid():
    new_event = form.save(commit=False)
    new_event.npo_id = npo_id
    new_event.save()
  return redirect('npos_detail', npo_id=npo_id)