from django.urls import path
from cases_app.api import views

# TEMPLATE TAGGING
app_name = 'cases_app_api'
urlpatterns = [
    path('', views.api_list_cases, name='api_list_cases'),
    path('update/<id>/', views.api_update_case, name='api_update_case'),
    path('delete/<id>/', views.api_delete_case, name='api_delete_case'),
    path('create/', views.api_create_case, name='api_create_case'),
]
