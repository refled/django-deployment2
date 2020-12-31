from django.conf.urls import url
from app_three import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index')
    #path('app_three/', include('app_three.urls')),
    #path('admin/', admin.site.urls),
]
