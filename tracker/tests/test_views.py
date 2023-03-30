from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tracker.models import Newspaper


class AnonymousPermDenied(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_anon_denied(self):
        redactor = get_user_model().objects.create_user(
            username="funny_ann",
            password="12345",
        )
        address = reverse(
            "tracker:redactor-update",
            kwargs={"pk": redactor.id}
        )
        request = self.client.get(address)
        self.assertNotEqual(request.status_code, "200")

    def test_create_anon_denied(self):
        address = reverse("tracker:redactor-create")
        request = self.client.get(address)
        self.assertTrue(request.status_code >= 300)


class SearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        Newspaper.objects.create(
            title="doctors joke",
            content="you don't want to know"
        )
        Newspaper.objects.create(
            title="new motor",
            content="100500 squirrel power"
        )
        Newspaper.objects.create(
            title=" black sheep",
            content="there is no matching text here!"
        )

    def test_driver_search(self):
        address = reverse("tracker:newspaper-list")
        response = self.client.get(address, data={"search_text": "To"})
        newspapers = Newspaper.objects.filter(title__icontains="to")
        self.assertEqual(
            list(newspapers),
            list(response.context["newspaper_list"])
        )
