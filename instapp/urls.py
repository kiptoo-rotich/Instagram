from django.conf import settings
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('',views.home,name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView,{"next_page":'/'}),
]