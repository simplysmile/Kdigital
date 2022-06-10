from django.urls import path
from . import views
app_name='Member'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
]
