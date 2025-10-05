from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name="register"),
    path('logout/', views.custom_logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('jobsingle/', views.job_single, name='jobsingle'),
    path('jobpost/', views.job_post, name='jobpost'),
    path('services/', views.services, name='services'),
    path('services_single/', views.services_single, name='services_single'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_single/', views.portfolio_single, name='portfolio_single'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('pjobsingle/<int:id>', views.pjob_single, name='pjobsingle'),
    path('upload-resume/', views.upload_resume, name='upload_resume'),
    
]
