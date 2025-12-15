from django.urls import path
from .views import job_list, job_create, job_update, job_delete, job_pdf

urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', job_create, name='job_create'),
    path('update/<int:id>/', job_update, name='job_update'),
    path('delete/<int:id>/', job_delete, name='job_delete'),

    path('pdf/', job_pdf, name='job_pdf'),
]