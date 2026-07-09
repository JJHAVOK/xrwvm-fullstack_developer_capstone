from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    
    # Explicit paths first
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
    
    # Static files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    # Catch-all ONLY for paths that do NOT start with admin/
    re_path(r'^(?!admin|djangoapp).*$', TemplateView.as_view(template_name="index.html")),
]