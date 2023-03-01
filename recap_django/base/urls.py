from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import  home, result, about, SignupPage
from . import views



urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
    path('result_with_no_text/', result, name='result_with_no_text'),
    path('about/', about, name='about'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('signup/get_api/', TemplateView.as_view(template_name="get_api.html"), name='get_api'),
]

