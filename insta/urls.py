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
    url(r'^comment$',views.makecomment,name='makecomment'),
    url(r'^(?P<object_id>[0-9]+)/delete_answer/$', views.deletephoto, name='deletephoto'),
    url(r'^like$',views.like_a_post,name='like_a_post'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)