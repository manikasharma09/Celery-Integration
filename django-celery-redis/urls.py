from django.contrib import admin
from django.urls import path
from app.views import BuildTrigger
from django.conf.urls import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'app/trigger_build/',BuildTrigger.as_view()),
]
