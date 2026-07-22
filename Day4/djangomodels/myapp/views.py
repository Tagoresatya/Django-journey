from django.http import JsonResponse
from django.shortcuts import redirect, render
from myapp.models import Student

# Create your views here. 

def student_create(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        rollno = request.POST['rollno']
        Student.objects.create(name=name, age=age, rollno=rollno)
        return redirect("home")
    return render(request, "myapp/studentcreate.html")



def student_update(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        age = request.POST['age']
        rollno = request.POST['rollno']
        student = Student.objects.get(id=id)
        student.name = name
        student.age = age
        student.rollno = rollno
        student.save()
        return redirect("home")
    return render(request, "myapp/studentupdate.html")




def student_get(request, id):
    student = Student.objects.get(id=id)
    d = {id: student.id, "name": student.name, "age": student.age, "rollno": student.rollno}
    return JsonResponse(d)
 


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("home")  





def home(request):
    students = Student.objects.all()
    return render(request, "myapp/home.html", {"students": students})   