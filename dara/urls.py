from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views
from dashboard import views as DashboardViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path('dashboard/', include('dashboard.urls')),

]

