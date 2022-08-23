from django.urls import path
from . import views

urlpatterns = [
     path('first-question/', views.firstquestionview.as_view(), name='first-question'),
     path('second-question/', views.secondquestionview.as_view(), name='second-question'),
     path('third-question/', views.thirdquestionview.as_view(), name='third-question'),
     path('success/', views.successview.as_view(), name='success'),
]