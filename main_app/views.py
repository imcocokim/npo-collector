from django.urls import reverse
from django.shortcuts import render,redirect
from .models import NPO, Event, Photo
from .forms import EventForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

# Add these "constant" variables below the imports
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'npo-collector'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def npos_index(request):
  npos = NPO.objects.all()
  return render(request, 'npos/index.html', {'npos': npos})

@login_required
def npos_detail(request, npo_id):
  npo = NPO.objects.get(id=npo_id)
  event_form = EventForm()
  return render(request, 'npos/detail.html', { 'npo': npo, 'event_form': event_form })

class NPOCreate(LoginRequiredMixin, CreateView):
  model = NPO
  fields = ['name', 'topic', 'description', 'website']
  success_url = '/npos/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class NPOUpdate(LoginRequiredMixin, UpdateView):
  model = NPO
  fields = ['topic', 'description', 'website']

class NPODelete(LoginRequiredMixin, DeleteView):
  model = NPO
  success_url = '/npos/'

@login_required
def add_event(request, npo_id):
  form = EventForm(request.POST)
  if form.is_valid():
    new_event = form.save(commit=False)
    new_event.npo_id = npo_id
    form.instance.user = request.user
    new_event.save()
  return redirect('npos_detail', npo_id=npo_id)

@login_required
def delete_event(request, npo_id, event_id):
  event = Event.objects.get(id=event_id)
  event.delete()
  return redirect('npos_detail', npo_id=npo_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('npos_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def add_photo(request, npo_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, npo_id=npo_id)
      cat_photo = Photo.objects.filter(npo_id=npo_id)
      if cat_photo.first():
        cat_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('npos_detail', npo_id=npo_id)
