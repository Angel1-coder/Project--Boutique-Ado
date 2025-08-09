from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # I'm including all the URL patterns for 'allauth' here.
    path('accounts/', include('allauth.urls')),
]

# This is the important part I added. In development, Django doesn't
# serve static and media files by default. I need to explicitly tell it to.
# This code block only runs if I'm in DEBUG mode.
if settings.DEBUG:
    # This tells Django to serve my media files (like the background image)
    # from the path defined by MEDIA_URL.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This tells Django to serve my static files (like my base.css)
    # from the path defined by STATIC_URL. I'm using STATICFILES_DIRS[0]
    # to get the exact directory I specified in my settings.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])