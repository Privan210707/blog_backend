from django.urls import path
from .views import hello_api,signup_api,profile_api
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns=[
    path('hello/',hello_api),
    path('signup/',signup_api),

    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('profile/',profile_api,name='profile'),
]