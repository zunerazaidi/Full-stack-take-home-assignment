from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import MyUser


def team_member_list(request):
    all_members = MyUser.objects.all
    member_count = MyUser.objects.all().count()
    return render(request, 'team_member_list.html', {'all_members': all_members, 'member_count': member_count})


def add_team_member(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
    # return render(request, 'add_team_member.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("logout")

def edit_team_member(request):
    return render(request, 'edit_team_member.html', {})
