from django.shortcuts import render
from . forms import StudentRegistration

def home(request):
    form = StudentRegistration()

    return render(request, 'enroll/home.html', {'form': form})