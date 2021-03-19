from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UseRegisterForm

def register(request):
    if request.method == 'POST':
        form = UseRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usename = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {usename}!')
            return redirect('cyber_blog-home')
    else:
        form = UseRegisterForm()
    return render(request, 'users/register.html', {'form': form})


