from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from home import views

urlpatterns = [
    path("", views.theme_list),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
