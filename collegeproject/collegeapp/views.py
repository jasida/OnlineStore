


from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Course
from django.shortcuts import render
from .forms import MyForm


def my_view(request):
    message = None
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            message = "Order Confirmed"
    else:
        form = MyForm()
    return render(request, 'template.html', {'form': form , 'message': message})


def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)


def index(request):
    return render(request,"index.html")



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('password1', '')

        if username and password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or passwords do not match')

    return render(request, 'register.html')


# def register(request):
#     if request.method == 'POST' :
#         username = request.POST['username','']
#         password = request.POST['password','']
#         cpassword = request.POST['password1','']
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'username taken')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save();
#                 messages.info(request, 'user created')
#         else :
#             messages.info(request, 'password not matching')
#             return redirect('register')
#         return render(request,'login.html')
#     return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'empty.html')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request,'form.html')



