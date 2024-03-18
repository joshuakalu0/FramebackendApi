from django.urls import path
from core.views import MyCreateViewClass, myTokenViewClass
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('user/',MyCreateViewClass,name= 'create-user'),
    path('token/',myTokenViewClass),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('token/verify/',TokenVerifyView.as_view())
]
