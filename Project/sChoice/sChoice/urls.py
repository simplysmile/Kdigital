from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('adminpage/',include('AdminPage.urls')),
    path('board/',include('Board.urls')),
    path('dailycheck/',include('DailyCheck.urls')),
    path('member/',include('Member.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)