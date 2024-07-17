from django.urls import path
from .views import content_form, content_data, content_update,content_delete


urlpatterns = [
    path('form/', content_form, name='form_url'),
    path('data/', content_data, name='data_url'),
    path('update/<int:pk>/', content_update, name='update_url'),
    path('delete/<int:pk>/', content_delete, name='delete_url'),

]