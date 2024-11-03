"""
URL configuration for finance_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryCreateView.as_view(), name="CategoryList"),
    path('category/<int:pk>/', CategoryCreateView.as_view(), name="CategoryDetail"), 
    path('transaction/', TransactionView.as_view(), name="TransactionList"),
    path('transaction/<int:pk>/', TransactionView.as_view(), name="TransactionDetail"), 
]
