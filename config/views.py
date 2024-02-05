import json

from django.http import HttpResponseNotFound
from django.views import View


class Json404View(View):
    def dispatch(self, request, *args, **kwargs):
        message = json.dumps({"message": "not found"})
        return HttpResponseNotFound(message, content_type="application/json")
