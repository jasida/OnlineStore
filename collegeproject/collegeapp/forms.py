
from django import forms
from .models import Department,Course



class MyForm(forms.Form):
    departments = Department.objects.all()
    department_choices = [(department.id, department.name) for department in departments]

    courses = Course.objects.all()
    course_choices = [(course.id, course.name) for course in courses]

    department = forms.ChoiceField(choices=[('', 'Select Department')] + department_choices)
    course = forms.ChoiceField(choices=[('', 'Select Course')] + course_choices)