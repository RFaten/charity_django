from django.urls import path
from donations_app.api import views

# TEMPLATE TAGGING
app_name = 'donations_app_api'
urlpatterns = [
    path('', views.api_list_donations, name='api_list_donations'),
    # path('update/<id>/', views.api_update_donation, name='api_update_donation'),
    # path('delete/<id>/', views.api_delete_donation, name='api_delete_donation'),
    path('create/', views.api_create_donation, name='api_create_donation'),
]
