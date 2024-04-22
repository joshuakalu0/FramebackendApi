from django.urls import path
from hello.views import index

app_name = 'hello'

urlpatterns = [
path('hello',index)
]