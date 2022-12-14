from django.views.generic import ListView, CreateView

from .models import Person


class PersonCreationView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')
    template_name = "persons/create.html"


class PersonListView(ListView):
    model = Person
    context_object_name = "persons"
    template_name = "persons/list.html"
