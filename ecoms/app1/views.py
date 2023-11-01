from django.shortcuts import render,redirect
from .models import Kids
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def kids(request):
    dict_kid={'kid':Kids.objects.all()}
    return render(request,'kids.html',dict_kid)


from .forms import RegistrationForm
def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

def logine(request):
  if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect('homepage')
      else:
          error_message = 'Invalid username or password.'
  else:
      error_message = None

  return render(request,'login.html',{'error_message':error_message})

def logout_user(request):
    logout(request)
    return redirect('login')
