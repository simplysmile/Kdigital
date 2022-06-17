from django.urls import path
from . import views
app_name='Board'
urlpatterns = [
    path('<int:nowpage>/exboard/',views.exboard,name='exboard'),
    path('<int:nowpage>/exwrite/',views.exwrite,name='exwrite'),
    path('<int:nowpage>/fdboard/',views.fdboard,name='fdboard'),
    path('<int:nowpage>/fdwrite/',views.fdwrite,name='fdwrite'),
    path('<int:bNo>/<int:nowpage>/exView/',views.exView,name='exView'),
    path('<int:bNo>/<int:nowpage>/fdView/',views.fdView,name='fdView'),
    path('shop/',views.shop,name='shop'),
]
