from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('parsed_data.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
