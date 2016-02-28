from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.templatetags.static import static
from oscar.app import application
from GamesOfFuture import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include(application.urls)),

    # for translations
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # url(r'^', include('shop.urls')),
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL)
