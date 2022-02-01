from django.shortcuts import render
from . forms import StudentRegistration
from . models import User

def home(request):
    form = StudentRegistration()
    stud = User.objects.all();

    return render(request, 'enroll/home.html', {'form': form, 'stud': stud})