from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include("dashboard.urls")),
    path('login/',views.custom_login ,name='login'),
    path('logout/', views.custom_logout ,name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view() ,name='password_reset'),
    path('reset-password/done', auth_views.PasswordResetDoneView.as_view() ,name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view() ,name='password_reset_complete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)