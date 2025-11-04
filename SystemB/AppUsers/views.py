from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def home(request):
    return render(request, 'Home.html')

def login(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        password = request.POST['password']

        user = authenticate(request, username=fullname, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'Login.html')

def register(request):
    if request.method == 'POST':
        fullname=request.POST.get( 'fullname' )
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=fullname).exists():
               print('Username exists')
               messages.error(request,'The username is taken,please enter another username')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
               print('The email exists')
               messages.info(request,'The email exists,please enter another username')
               return redirect('register')
            else:
               user=User.objects.create_user(username=fullname,email=email,password=password)
               user.save()
               messages.success(request, 'Registration successful! You can now log in.')
               return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

    else:
      return render(request,'Register.html')
    
def logout(request):
    auth_logout(request)
    return redirect('register')
