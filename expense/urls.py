from django.urls import include, path
from . import views


app_name='expense'
urlpatterns = [
    #ex: /expense/
    path('', views.index,name='index'), 
    path('add', views.add, name='add'),
    path('<int:id>/delet', views.delet, name='delet'),
   
]