from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'mainpage.views.mainpage',name='mainpage'),
    url(r'^user1/', 'mainpage.views.user1',name='user1'),
    url(r'^admincall/', 'mainpage.views.admincall'),
    url(r'^admin/', admin.site.urls),
]
