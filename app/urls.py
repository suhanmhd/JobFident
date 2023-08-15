from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('rctrhome',views.rctrhome,name='rctrhome'),
    path('jobpost',views.jobpost,name='jobpost'),
    path('newpost',views.newposts,name='newpost'),
    path('categoryjob<str:pk>',views.categoryjob,name='categoryjob'),
    path('blog',views.blog, name='blog'),
    path('blogsingle',views.blogsingle,name='blogsingle'),
    path('browsejobs',views.browsejobs,name='browsejobs'),
    path('candidates',views.candidates,name='candidates'),
    path('contact',views.contact,name='contact'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
     path('rctrlogout',views.rctr_logout,name='rctrlogout'),
    path('signup',views.register,name='signup'),
    path('rctrlogin',views.rctr_login,name='rctrlogin'),
    path('rctrsignup',views.rctr_register,name='rctrsignup'),
    path('apply<str:pk>',views.apply,name='apply'),
    path('viewapplicant',views.viewapplicant, name='viewapplicant'),
    path('applicantdetail<str:pk>',views.applicantdetail,name='applicantdetail'),
    path('appliedjobs',views.userappliedjobs, name='userappliedjobs'),
    path('postedjobs',views.postedjobs, name='postedjobs'),
    path('deleteappliedjobs<str:pk>',views.deleteappliedjobs,name='deleteappliedjobs'),
    path('deletepostedjobs<str:pk>',views.deletepostedjobs,name='deletepostedjobs'),
    path('applicationtstatus<str:pk>',views.applicationtstatus,name='applicationtstatus'),
    path('applicationreject<str:pk>',views.applicationreject,name='applicationreject'),

   
   
  
    
    
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)