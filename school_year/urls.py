from django.urls import path
from . import views

app_name = 'school_year'

urlpatterns = [
	path('', views.index, name='list')
]
