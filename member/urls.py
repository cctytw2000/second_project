from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forget/',views.forget,name='forget'),
    path('create',views.create,name='create')
]