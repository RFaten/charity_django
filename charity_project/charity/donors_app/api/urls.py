from django.urls import path
from donors_app.api import views

# TEMPLATE TAGGING
app_name = 'donors_app_api'
urlpatterns = [
    path('', views.api_list_donors, name='api_list_donors'),
    path('update/<id>/', views.api_update_donor, name='api_update_donor'),
    path('delete/<id>/', views.api_delete_donor, name='api_delete_donor'),
    path('create/', views.api_create_donor, name='api_create_donor'),
]
