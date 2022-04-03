"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# https://github.com/alanjds/drf-nested-routers
from django.urls import path, re_path
from api import views
from rest_framework import routers
from django.conf.urls import include
from api.views import TrackView

router = routers.DefaultRouter()
router.register('chart', views.ChartView, basename='chart')
# router.register(r'^track/(?P<pk>\.+)/$', views.TrackView, basename='track')

urlpatterns = [
    path(r'', include(router.urls)),
    path('track/<str:pk>', TrackView.as_view())
]
