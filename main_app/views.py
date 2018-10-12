from django.shortcuts import render
from .models import Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import  LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def skills_index(request):
    skills = Skill.objects.all()
    return render(request, 'skills/index.html', { 'skills': skills} )

def index(request):
    return render(request, 'base.html')

def skills_detail(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    return render(request, 'skills/detail.html', {'skill': skill})

class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'
    success_url = '/skills'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/skills/')

class SkillUpdate(UpdateView):
    model = Skill
    fields = ['skill', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/skills/' + str(self.object.pk))

class SkillDelete(DeleteView):
    model = Skill
    success_url = '/skills'

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
@login_required
def profile(request, username):
    if username == request.user.username:    
        user = User.objects.get(username=username)
        skills = Skill.objects.filter(user=user)
        return render(request, 'profile.html', {'username': username, 'skills': skills})
    else:
        return HttpResponseRedirect('/')


