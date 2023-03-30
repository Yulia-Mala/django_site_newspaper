from django.test import TestCase

from tracker.forms import RedactorForm


class RedactorFormTests(TestCase):
    def setUp(self):
        self.redactor_data = {
            "username": "new_buddy",
            "password1": "qWertY9876543",
            "password2": "qWertY9876543",
            "first_name": "Test",
            "last_name": "Testovych",
            "years_of_experience": 5
        }

    def test_creation_form_is_valid(self):
        redactor_form = RedactorForm(self.redactor_data)
        self.assertTrue(redactor_form.is_valid())
        self.assertEqual(redactor_form.cleaned_data, self.redactor_data)

    def test_creation_form_is_not_valid(self):
        not_valid_data = self.redactor_data.copy()
        not_valid_data["years_of_experience"] = -1
        redactor_form = RedactorForm(not_valid_data)
        self.assertFalse(redactor_form.is_valid())
