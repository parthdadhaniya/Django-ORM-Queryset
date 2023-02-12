from django.shortcuts import render
from quryset_app.models import Student


# Create your views here.

def home(request):
    """All Method in Queryset its will return New Queryset"""
    # student_data = Student.objects.all()

    """Filter Method in Queryset its will return New Queryset"""
    # student_data = Student.objects.filter(marks=70)

    """Exclude Method in Queryset its will return New Queryset"""
    # student_data = Student.objects.exclude(marks=70)

    """order_by(fields) Method in Queryset its will return New Queryset and asc Value"""
    # student_data = Student.objects.order_by('city')

    """order_by(-fields) Method in Queryset its will return New Queryset and dec Value"""
    # student_data = Student.objects.order_by('-city')

    """order_by(?) Method in Queryset its will return New Queryset and randomly Value"""
    student_data = Student.objects.order_by('?')
    return render(request, 'quryset/home.html', {'students': student_data})
