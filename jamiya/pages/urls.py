from django.urls import path
from .views import page_view

urlpatterns = [
    path('<str:lang>/<slug:slug>/', page_view),
]