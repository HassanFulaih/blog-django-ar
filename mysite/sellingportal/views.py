from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from sellingportal import models, forms


def my_index(request):
    return render(request, 'index.html')


def my_home(request):
    return render(request, 'home.html')


def student(request):
    students = models.Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def student_degree(request, st_id):
    degree = models.Degree.objects.filter(student_id=st_id)
    students = models.Student.objects.get(id=st_id)
    form_data = forms.DegreeRegistrar(request.POST or None)
    if form_data.is_valid():
        d_degree = models.Degree()
        d_degree.student_degree = form_data.cleaned_data['student_degree']
        d_degree.student_id = students
        d_degree.save()
    context = {'degree': degree, 'form_register': form_data}
    return render(request, 'degree.html', context)


def register(request):
    form_data = forms.UserRegistrar(request.POST or None)
    if form_data.is_valid():
        s_student = models.Student()
        s_student.first_name = form_data.cleaned_data['first_name']
        s_student.last_name = form_data.cleaned_data['last_name']
        s_student.age = form_data.cleaned_data['age']
        s_student.date_birth = form_data.cleaned_data['date_birth']
        s_student.save()
    context = {'form_register': form_data}
    return render(request, 'register.html', context)
