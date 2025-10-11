from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("add/", views.add_request, name="add_request"),
    path("donate/<int:id>", views.donate, name="donate")
]