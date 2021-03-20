from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserRegistrationForm


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        # messages.success(request, 'Пользователь добавлен в систему.')
        # return render(request, 'accounts/register_done.html',
        #               {'new_user': new_user})
        return redirect('/login/')
    return render(request, 'accounts/register.html', {'form': form})