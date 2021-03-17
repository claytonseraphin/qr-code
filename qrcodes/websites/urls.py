from django.urls import path, include
from . import views

app_name = 'websites'
urlpatterns = [
	path('', views.QrView.as_view(), name='qr'),
]
