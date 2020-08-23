from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
class HomePageTests(SimpleTestCase):
    def testHomePageStatusCode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testViewUrlByName(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def testViewUsesCorrectTemplate(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    username = 'new_user'
    email = 'new_user@email.com'

    def testSignupPageStatusCode(self):
        response = self.client.get('/user/signup/')
        self.assertEqual(response.status_code, 200)

    def testViewUrlByName(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def testViewUsesCorrectTemplate(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def testSignupForm(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
