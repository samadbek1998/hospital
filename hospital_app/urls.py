from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('service/', views.service_page_view, name='service'),
    path('team/', views.team_page_view, name='team'),
    path('feature/', views.feature_page_view, name='feature'),
    path('appointment.html/', views.appointment_page_view, name='appointment'),
    path('testimonial/', views.testimonial_page_view, name='testimonial'),
    path('error/', views.error_404_view, name='error'),  
]