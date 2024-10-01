from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pvrcblog/', views.pvrcblog, name='pvrcblog'),
    #path('signin/', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('sinout/',views.sinout,name='sinout'),
    path('contact/', views.contact, name='contact'), 
    path('update/<int:id>/update/', views.update, name='update'),
    path('contact/<int:id>/delete/', views.contact, name='contact'),  # Updated URL for delete
    path('down/',views.down,name='down'),
    path('register/', views.register, name='register'),
   # path('page_404/',views.page_404,name='page_404')

]