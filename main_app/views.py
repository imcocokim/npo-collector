from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

# def npos_index(request):
#   return render(request, 'npos/index.html', {'npos': npos})