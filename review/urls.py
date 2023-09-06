from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.rate, name='create_review'),
    path('success', views.success, name='success'),
    path('rate/<int:id>/', views.rate, name='rate'),
]
