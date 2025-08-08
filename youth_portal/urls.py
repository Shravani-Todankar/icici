from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz/<int:pdf_id>/', views.quiz_view, name='quiz'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)