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
    path('<int:bNo>/<int:nowpage>/exBUP/',views.exBUP,name='exBUP'),
    path('<int:bNo>/<int:nowpage>/fdBUP/',views.fdBUP,name='fdBUP'),
    path('<int:bNo>/<int:nowpage>/exDel/',views.exDel,name='exDel'),
    path('<int:bNo>/<int:nowpage>/fdDel/',views.fdDel,name='fdDel'),
    path('shop/',views.shop,name='shop'),
]
