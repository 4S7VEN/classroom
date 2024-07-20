from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as auth_logout, authenticate
from .forms import SignUpForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirects to a login page or specific page
    else:
        form = SignUpForm()
    return render(request, 'signup_form.html', {'form': form})


@login_required
def loginType(request):
    user = request.user
    # Determine if the user is a student or teacher
    if user.user_type == 2:
        return redirect('student_home')  # Ensure 'student_home' is defined in urls.py
    elif user.user_type == 1:
        return redirect('teacher_home')  # Ensure 'teacher_home' is defined in urls.py
    else:
        return redirect('login')


@login_required
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request=request))


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def student_home(request):
    return render(request, 'student_dashboard.html')


@login_required
def teacher_home(request):
    return render(request, 'teacher_dashboard.html')
