from django.urls import path
from billing import views

app_name = 'billing'

urlpatterns = [
    path('', views.billing, name='list'),
    path('history/', views.billing_history, name='history'),
]
