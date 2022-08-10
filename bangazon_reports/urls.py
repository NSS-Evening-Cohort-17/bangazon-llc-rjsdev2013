from django.urls import path
from .views import ProductListOver1000

urlpatterns = [
    path('1000', ProductListOver1000.as_view()),
]