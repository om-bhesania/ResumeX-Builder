from django.contrib import admin
from django.urls import path
from builder import views



app_name = 'builder'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('ai-build-helper/', views.ai, name='ai'),
    path('chat/', views.generate_chat_response, name='chat'),
    path('login/', views.login_view, name='login_view'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('builder/', views.builder, name='builder'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('process/', views.process, name='process'),
    path('upload/', views.document_upload, name='document_upload'), 
    path('contact/', views.contact, name='contact'),
    path('template1/', views.template1, name='template'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('product/<int:pk>/editResume', views.edit_product, name='edit_product'),
] 

 