# from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth.models import User
# from django.shortcuts import render,redirect

# def home(request):
#     return render(request, 'Home.html')

# def login(request):
#     if request.method == 'POST':
#         fullname = request.POST['fullname']
#         password = request.POST['password']

#         user = authenticate(request, username=fullname, password=password)

#         if user is not None:
#             auth_login(request, user)
#             return redirect('register')
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, 'Login.html')

# def register(request):
#     if request.method == 'POST':
#         fullname=request.POST.get( 'fullname' )
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         confirm_password=request.POST.get('confirm_password')

#         if password == confirm_password:
#             if User.objects.filter(username=fullname).exists():
#                print('Username exists')
#                messages.error(request,'The username is taken,please enter another username')
#                return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                print('The email exists')
#                messages.info(request,'The email exists,please enter another username')
#                return redirect('register')
#             else:
#                user=User.objects.create_user(username=fullname,email=email,password=password)
#                user.save()
#                messages.success(request, 'Registration successful! You can now log in.')
#                return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match.')
#             return redirect('register')

#     else:
#       return render(request,'Register.html')
    
# def logout(request):
#     auth_logout(request)
#     return redirect('register')

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import UserProfile

def home(request):
    return render(request, 'Home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            user = User.objects.create_user(
                username=cleaned_data['email'],
                email=cleaned_data['email'],
                password=cleaned_data['password'],
                first_name=cleaned_data['fullname']
            )
            
            # Create UserProfile
            profile = form.save(commit=False)
            profile.user = user
            profile.fullname = cleaned_data['fullname']
            profile.email = cleaned_data['email']
            profile.save()
            
            # Auto login after registration
            user = authenticate(
                username=cleaned_data['email'],
                password=cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.success(request, 'Registration successful! Welcome!')
                return redirect('home')  # Change to your success page
            
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']  
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def profile(request):
    profile = request.user.userprofile  # Access the profile
    return render(request, 'profile.html', {'profile': profile})
    
def logout(request):
    auth_logout(request)
    return redirect('register')