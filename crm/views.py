from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm 
from .models import Record 

def home(request):
  records = Record.objects.all()
  return render(request, 'crm/home.html', {'records': records})


def user_login(request):
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are logged in')
      return redirect('home')
    else:
      messages.error(request, 'Username or Password is incorrect')
      return redirect('login')
  else:
    return render(request, 'crm/login.html')
  
# logout function
def user_logout(request):
  auth.logout(request)
  messages.success(request, 'You are logged out')
  return redirect('home')


def user_register(request):
  form = CustomUserCreationForm()
  
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'Account was created for ' + user)
      return redirect('login')
  
  else:   
    context = {'form': form}
    return render(request, 'crm/register.html', context)
  
def user_record(request, pk):
  # not to allow not login user to access it
  if request.user.is_authenticated:   
    # view the record
    user_record = Record.objects.get(id=pk)
    return render(request, 'record.html', {'user_record':user_record})
  
  else:
    messages.success(request, 'You must be logged in to view this page ')
    return redirect('home')

# def user_register(request):
#   if request.method == 'POST':
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     confirm_password = request.POST.get('confirm-password')

#     if password == confirm_password:
#       if User.objects.filter(username=username).exists():
#         messages.error(request, 'Username already exists')
#         return redirect('register')
#       else:
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.set_password(password)
#         user.save()
#         messages.success(request, 'User registered successfully')
#         return redirect('login')
      
#     else:
#       messages.error(request, 'Username or Password do not match')
#       return redirect('register')
    
#   else:
#     return render(request, 'crm/register.html')