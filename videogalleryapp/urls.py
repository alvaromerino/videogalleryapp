from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from gallery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^gallery/', include('gallery.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Video Gallery Admin"
admin.site.site_title = "Video Gallery Admin Portal"
admin.site.index_title = "Welcome to Video Gallery Portal"
