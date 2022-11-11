from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignUpForm


# Create your tests here.
class TestIsUserAuth(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")

    def test_user(self):
        self.client.login(username="test", password="test")
        assert self.user.is_authenticated

    def test_user_can_login(self):
        login = self.client.login(username="test", password="test")
        self.assertEquals(login, True)

    def test_user_cant_login_with_wrong_password(self):
        login = self.client.login(username="test", password="hfhf")
        self.assertEquals(login, False)

    def test_user_cant_see_signup_page(self):
        self.client.login(username="test", password="test")
        response = self.client.get("signup")
        assert response.status_code == 404

    def test_user_cant_see_login_page(self):
        self.client.login(username="test", password="test")
        response = self.client.get("login")
        assert response.status_code == 404

    # def test_cant_login_with_username_that_is_taken(self):
    #     form = SignUpForm
    #     form.username = "test"
    #     form.email = "test@test.com"
    #     form.password1 = "test"
    #     form.password2 = "test"
    #     self.assertFormError(form, "username", "Username already exists")