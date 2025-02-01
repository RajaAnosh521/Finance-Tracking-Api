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
from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, TransactionListCreateView, TransactionRetrieveUpdateDestroyView

urlpatterns = [
    # Category Endpoints
    path('category/', CategoryListCreateView.as_view(), name="category-list-create"),  # Handles GET (list) & POST (create)
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name="category-detail"),  # Handles GET (retrieve), PUT (update), DELETE (delete)

    # Transaction Endpoints
    path('transaction/', TransactionListCreateView.as_view(), name="transaction-list-create"),  # Handles GET (list) & POST (create)
    path('transaction/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view(), name="transaction-detail"),  # Handles GET (retrieve), PUT (update), DELETE (delete)
]
