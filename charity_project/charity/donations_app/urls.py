from django.urls import path
from donations_app import views

# TEMPLATE TAGGING
app_name = 'donations_app'
urlpatterns = [
    path('', views.donations, name='donations'),
    path('create_donation/', views.create_donation, name='create_donation'),
    path('<id>/', views.update_donation, name='update_donation'),
    path('delete/<int:donation_id>', views.delete_donation, name='delete_donation'),
]
