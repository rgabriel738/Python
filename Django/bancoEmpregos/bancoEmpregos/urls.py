from django.contrib import admin
from django.urls import path
from vagas.views import *  
from django.conf.urls.static import static 
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/chart/data/$', ChartData.as_view(), name='graficos'),
    url(r'^$', HomeView.as_view(), name='home'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
