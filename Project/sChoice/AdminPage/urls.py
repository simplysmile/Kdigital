from django.urls import path
from . import views
app_name='AdminPage'
urlpatterns = [
    path('',views.aboutus,name='index'),
    
]
