from django.urls import path
from donors_app import views

# TEMPLATE TAGGING
app_name = 'donors_app'
urlpatterns = [
    path('', views.donors, name='donors'),
    path('create_donor/', views.create_donor, name='create_donor'),
    path('<id>/', views.update_donor, name='update_donor'),
    path('delete/<int:donor_id>', views.delete_donor),
]
