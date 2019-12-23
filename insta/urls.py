from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^search/',views.search_category,name='search_category'),
    url(r'^photo/(\d+)',views.single_photo,name='photo'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)