from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentForm

# Create your views here.

def home(request):
    students = Student.objects.all()
    data = {"students": students}
    return render(request, 'students/home.html', data)

def create(request):
    form = StudentForm()
    if( request.method == "POST"):
        form = StudentForm(request.POST)
        if( form.is_valid() ):
            form.save()
            return redirect('/')

    data = {"form": form}
    return render(request, 'students/create.html', data)

def update(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if( request.method == "POST" ):
        form = StudentForm(request.POST, instance=student)
        if( form.is_valid() ):
            form.save()
            return redirect('/')

    data = {"student": student, "form": form}
    return render(request, 'students/update.html', data)

def delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/')