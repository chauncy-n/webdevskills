from django.shortcuts import render
from .models import Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect


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

class SkillUpdate(UpdateView):
    model = Skill
    fields = ['skill', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/skills' + str(self.object.pk))
