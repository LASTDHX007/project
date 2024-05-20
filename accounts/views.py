from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth import login, authenticate 
from .forms import UserRegistrationForm 



# Create your views here.
@login_required
def profile(request):
    context={
        'session':'profile',
    }
    return render(request,'accounts/profile.html',context)


def register(request): 
    if request.method == 'POST' : 
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=password)
            login(request,user)  
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')    
            return redirect('login') 
    else : 
        form = UserRegistrationForm() 
    return render(request,'accounts/registration.html',{'form' : form}) 