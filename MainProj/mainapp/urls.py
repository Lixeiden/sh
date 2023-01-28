from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.List.as_view(), name='list'),
    path('pub-<str:uri>/', views.Pub.as_view(), name='pub'),
    path('', views.Add.as_view(), name='add'),
    path('all/', views.AllEntries.as_view()),
    path('get-<str:uri>/', views.OneEntry.as_view()),
]
