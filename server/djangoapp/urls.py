# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Keep these as the API endpoints
    path('register', views.registration, name='register'), # API
    path('login', views.login_user, name='login'), # API
    path('logout', views.logout_request, name='logout'), # API
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
