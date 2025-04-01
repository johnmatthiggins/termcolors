from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from home import views

urlpatterns = [
    path("", views.theme_list),
    path("preview/<str:slug>/", views.theme_view),
    path("download/windows/<str:slug>/", views.download_theme_windows_terminal),
    path("download/alacritty/<str:slug>/", views.download_theme_alacritty),
    path("download/kitty/<str:slug>/", views.download_theme_kitty),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
