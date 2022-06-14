from django.urls import path
from . import views
app_name='AdminPage'
urlpatterns = [
    path('',views.aboutus,name='index'),
    path('<str:searchword>/<str:category>/ad_m_L/',views.ad_m_L, name='ad_m_L'),
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_V/',views.ad_m_V, name='ad_m_V'),
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_U/',views.ad_m_U, name='ad_m_U'),
    path('aboutus/',views.aboutus, name='aboutus'),
]

    

