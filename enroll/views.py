import imp
from unittest import registerResult
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . forms import StudentRegistration
from . models import User
from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = StudentRegistration()
    stud = User.objects.all();
    return render(request, 'enroll/home.html', {'form': form, 'stud': stud})

#@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            if sid == '':
                usr = User(name = name, email = email, password = password)
            else:
                 usr = User(id = sid, name = name, email = email, password = password)

            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            #print(student_data)
            return JsonResponse({'status': 'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status': 0})

#@csrf_exempt
def delete_data(request):

   # print(request.POST.get('sid'))
    
     if request.method == 'POST':
         id = request.POST.get('sid')
         print(id)
         pi = User.objects.get(id=id)
         pi.delete()

         return JsonResponse({'status': 1})
     else:    

        return JsonResponse({'status': 0})



def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)

        student = User.objects.get(id = id)
        student_data = {"id": student.id, "name": student.name, "email": student.email, "password":student.password}

        return JsonResponse(student_data)


