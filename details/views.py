from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

from details.forms import ProfileForm
from details.models import ProfileModel

from details.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'details/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login_page')
    else:
        form = SignUpForm()
    return render(request, 'details/signup_form.html', {'form': form})


@login_required
def profile_view(request):
    user = User.objects.all()
    users = ProfileModel.objects.all()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        print(request.user)
        if form.is_valid():
            if form.cleaned_data['role'] == 'N':
                request.user.is_superuser = False
                form.save()
                request.user.save()
            elif form.cleaned_data['role'] == 'A':
                request.user.is_superuser = True
                form.save()
                request.user.save()
                print(request.user.is_superuser)
            return HttpResponse('Your form is created...!')
    else:
        form = ProfileForm()
    return render(request, 'details/user_details.html', {'form': form})
