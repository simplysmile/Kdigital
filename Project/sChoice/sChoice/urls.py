from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('AdminPage/',include('AdminPage.urls')),
    path('Board/',include('Board.urls')),
    path('DailyCheck/',include('DailyCheck.urls')),
    path('Member/',include('Member.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)