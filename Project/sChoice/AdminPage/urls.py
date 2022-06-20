from django.urls import path
from . import views
app_name='AdminPage'
urlpatterns = [
    path('',views.aboutus,name='index'),
    path('aboutus/',views.aboutus, name='aboutus'),
    
    #admin login 
    path('ad_login/',views.ad_login,name="ad_login"),
    #admin logout
    path('ad_logout/',views.ad_logout,name="ad_logout"),
    #문의사항페이지
    path('ad_contact_us/',views.ad_contact_us, name='ad_contact_us'),
    ###########################################################################################
    
    #admin회원list
    path('<str:searchword>/<str:category>/ad_m_L/',views.ad_m_L, name='ad_m_L'),
    #admin회원view
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_V/',views.ad_m_V, name='ad_m_V'),
    #admin회원update
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_U/',views.ad_m_U, name='ad_m_U'),
    #admin회원delete
    path('<str:searchword>/<str:category>/<str:user_id>/ad_m_D/',views.ad_m_D, name='ad_m_D'),
    ###########################################################################################
    
    
    #admin음식list
    path('<str:searchword2>/<str:category2>/ad_f_L/',views.ad_f_L, name='ad_f_L'),
    #admin음식view
    path('<str:searchword2>/<str:category2>/<str:f_NO>/ad_f_V/',views.ad_f_V, name='ad_f_V'),
    #admin음식update
    path('<str:searchword2>/<str:category2>/<str:f_NO>/ad_f_U/',views.ad_f_U, name='ad_f_U'),
    #admin음식delete
    path('<str:searchword2>/<str:category2>/<str:f_NO>/ad_f_D/',views.ad_f_D, name='ad_f_D'),
    
    
    ###########################################################################################

    #admin운동list
    path('<str:searchword3>/<str:category3>/ad_e_L/',views.ad_e_L, name='ad_e_L'),
    #admin운동view
    path('<str:searchword3>/<str:category3>/<str:ex_id>/ad_e_V/',views.ad_e_V, name='ad_e_V'),
    #admin운동delete
    path('<str:searchword3>/<str:category3>/<str:ex_id>/ad_e_D/',views.ad_e_D, name='ad_e_D'),
    #admin운동update
    path('<str:searchword3>/<str:category3>/<str:ex_id>/ad_e_U/',views.ad_e_U, name='ad_e_U'),
    
    
    ###########################################################################################
    
    #admin문의list
    path('<str:searchword4>/<str:category4>/ad_c_L/',views.ad_c_L, name='ad_c_L'),
    #admin문의view
    path('<str:searchword4>/<str:category4>/<str:c_No>/ad_c_V/',views.ad_c_V, name='ad_c_V'),
    #admin문의update
    path('<str:searchword4>/<str:category4>/<str:c_No>/ad_c_U/',views.ad_c_U, name='ad_c_U'),
    #admin문의delete
    path('<str:searchword4>/<str:category4>/<str:c_No>/ad_c_D/',views.ad_c_D, name='ad_c_D'),
    
    
    
    
]