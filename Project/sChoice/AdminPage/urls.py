from django.urls import path
from . import views
app_name='AdminPage'
urlpatterns = [
    path('',views.aboutus,name='index'),
    #admin회원list
    path('<str:searchword>/<str:category>/ad_m_L/',views.ad_m_L, name='ad_m_L'),
    #admin회원view
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_V/',views.ad_m_V, name='ad_m_V'),
    #admin회원update
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_U/',views.ad_m_U, name='ad_m_U'),
    #admin음식list
    path('<str:searchword2>/<str:category2>/ad_f_L/',views.ad_f_L, name='ad_f_L'),
    #admin운동list
    path('<str:searchword3>/<str:category3>/ad_e_L/',views.ad_e_L, name='ad_e_L'),
    
    path('aboutus/',views.aboutus, name='aboutus'),
]
