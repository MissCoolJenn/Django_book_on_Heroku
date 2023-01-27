from django.urls import path
from .views import HomePage, AboutPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    #                   ^ always need when i use Class=Based views
    path('about/', AboutPage.as_view(), name='about'),
]