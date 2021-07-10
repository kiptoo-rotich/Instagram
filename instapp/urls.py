from django.conf import settings
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns =[
    path('',views.home,name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('register/', views.registrationPage,name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView,{"next_page":'/'}),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)