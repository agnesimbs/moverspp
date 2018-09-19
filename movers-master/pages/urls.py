from django.urls import path
from  .views import *
urlpatterns=[
path('',HomePageView.as_view(),name='home'),
path('about/',AboutPageView.as_view(),name='about'),
path('category/',CategoryView.as_view(),name='category'),
path('audio/',AudioView.as_view(),name='audio'),
path('gallery/',GalleryView.as_view(),name='gallery'),
path('standard/',StandardView.as_view(),name='standard'),
path('video/',VideoView.as_view(),name='video'),
path('guide/',GuideView.as_view(),name='guide'),
path('contact/',ContactView.as_view(),name='contact'),
path('login/',LoginView.as_view(),name='login'),
path('loginhandler/',loginHandler,name='login'),
path('signup/',SignUpView.as_view(),name='signup'),
path('mapping/',MappingView.as_view(),name='mapping'),
path('booking/',BookingView.as_view(),name='booking'),
path('bookinghandler/',bookinghandler,name='booking'),

#url(r"^checkout$", views.checkout, name="checkout_page"),

]