from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name = 'hello'),
    path('officers/', views.all_officers, name = 'all officers'),
    path('officers/<int:officer_id>/', views.one_officer, name = 'one officer'),
]
