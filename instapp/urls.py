from django.conf import settings
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('',views.home,name='home'),    
    path('comment/<id>', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
    path('search/',views.search_results,name='search'),
    path('newpost/', views.new_post, name='new_post'),
    path('detail/<image_id>',views.details, name='details'),
    path('accounts/register/', views.registrationPage,name='registration'),   
    
    path('accounts/login/',auth_views.LoginView.as_view(template_name='django_registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='navbar.html'),name='logout'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    