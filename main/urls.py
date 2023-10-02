from django.urls import path
from . import views


urlpatterns = [
    path("", views.ModelsViews.as_view(), name='modelsviews'),
]