from django.urls import path

from .views import PersonCreationView, PersonListView

app_name = "persons"

urlpatterns = [
    path('new/', PersonCreationView.as_view(), name="create"),
    path('', PersonListView.as_view(), name="list"),
]
