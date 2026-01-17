from django.shortcuts import render,redirect,get_object_or_404
from students.forms import StudentForm
from students.models import Student


# Create your views here.

def student_created(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request,'students/student_form.html',{'form':form})


def student_list(request):
    students = Student.objects.all()
    return render(request,'students/student_list.html',{'students':students})


def student_update(request,id):
    student = get_object_or_404(Student,id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request,'students/student_form.html',{'form':form})

def student_delete(request,id):
    student = get_object_or_404(Student,id=id)
    student.delete()
    return redirect('student_list')