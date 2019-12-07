from django.conf.urls import url
from gallery import views

# SET THE NAMESPACE!
app_name = 'gallery'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^$', views.gallery, name='index'),
]
