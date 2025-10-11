from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("add/", views.add_request, name="add_request"),
    path("donate/<int:id>", views.donate, name="donate"),
    path("api", views.api_requests, name="api_requests"),
    path("api/add/", views.api_add_request, name="api_add_request"),
    path("api/donate/", views.api_donate, name="api_donate"),
]