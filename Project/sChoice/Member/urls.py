from django.urls import path
from . import views
app_name='Member'
urlpatterns = [
    path('cancel_signup/',views.cancel_signup,name='cancel_signup'),
    #로그인입력취소
    path('signup/',views.signup,name='signup'),
    #로그인 페이지 연결
    path('login/',views.login,name='login'),
    # #로그아웃 페에지 연결
    path('logout/',views.logout,name='logout'),
    #나의정보 페에지 연결
    path('mView/',views.mView,name='mView'),
    # 회원 삭제 페에지 연결
    path('mDelete/',views.mDelete,name='mDelete'),
    #내 정보수정
    path('mUpdate/',views.mUpdate,name='mUpdate'),

]