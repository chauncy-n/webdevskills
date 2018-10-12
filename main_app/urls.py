from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skills/', views.skills_index, name='skills_index'),
    path('skills/<int:skill_id>', views.skills_detail, name='detail'),
]
