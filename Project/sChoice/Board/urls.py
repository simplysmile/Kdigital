from django.urls import path
from . import views
app_name='Board'
urlpatterns = [
    path('exboard/',views.exboard,name='exboard'),
]
