import json

from django.test import RequestFactory, TestCase

from config.views import Json404View


class Json404ViewTest(TestCase):
    def test_dispatch_method_directly(self):
        factory = RequestFactory()
        request = factory.get("/")

        view = Json404View()

        response = view.dispatch(request)
        response_content = json.loads(response.content.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response["content-type"], "application/json")
        self.assertEqual(response_content, {"message": "not found"})
