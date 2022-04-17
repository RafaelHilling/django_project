import django.http
from django.views import generic


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpReponse("Hello World")

