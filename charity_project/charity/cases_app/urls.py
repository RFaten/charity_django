from django.urls import path
from cases_app import views

# TEMPLATE TAGGING
app_name = 'cases_app'
urlpatterns = [
    path('', views.cases, name='cases'),
    path('create_case/', views.create_case, name='create_case'),
    path('<id>/', views.update_case, name='update_case'),
    # path('delete/<id>', views.delete_case, name='delete_case'),
    path('delete/<int:case_id>', views.delete_case),
]
