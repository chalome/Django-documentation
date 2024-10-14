"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path,include
from django_polls.views import *

urlpatterns = [
    # path("polls/", include("django_polls.urls")),
    path("admin/", admin.site.urls),
    # path("<int:question_id>/", detail,name='detail'),
    # path("<int:question_id>/results/", results,name='results'),
    path("<int:question_id>/vote/", vote,name='vote'),
    # path("", index,name='list'),
    path("", IndexView.as_view(),name='list'),
    path("<int:pk>/", DetailView.as_view(),name='detail'),
    path("<int:pk>/results/", ResultView.as_view(),name='results'),
]
