from django.urls import path
from .views import CreateViewUser, ViewSuccess

urlpatterns = [
    path('user/', CreateViewUser.as_view(), name='user'),
    path('success/', ViewSuccess.as_view(), name='success'),
]
