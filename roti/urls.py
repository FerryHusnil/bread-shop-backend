from django.urls import path
from .views import *

urlpatterns = [
    path('', RotiModelListView.as_view()),
    path('<int:roti_id>', RotiModelDetailView.as_view()),
]