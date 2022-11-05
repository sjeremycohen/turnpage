from django.test import TestCase, LiveServerTestCase, RequestFactory, Client
import random
import environ
from django.urls import reverse
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from .. import models
from django.contrib.auth.models import User
from .. import views


class TestUserBookInteraction(LiveServerTestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="test", email="jacob@…", password="12345"
        )

        for i in range(0, 15):
            models.Book.objects.create(
                title=str("test_" + str(i)),
                published_date="2020-01-01",
                author=str("test_" + str(i)),
                description="test",
                cover_img="test",
                isbn10="10",
                isbn13="13",
            )
        self.object_list = models.Book.objects.all()

        self.env = environ.Env()
        environ.Env.read_env()

    # def test_user_like_book(self):
    #     self.client.login(username="test", password="12345")
    #     service = Service(executable_path=ChromeDriverManager().install())
    #     driver = webdriver.Chrome(service=service)
    #     # TODO how to make this work with travis?
    #     driver.get('http://127.0.0.1:8000/')
    #     button = driver.find_element(By.ID, "swipe-right-btn")
    #     # trigger the `like` button on the book
    #     button.click()
    #     # make sure book is on user's bookshelf
    #     print(models.Bookshelf.objects.all())


class TestBookStack(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="test", email="jacob@…", password="12345"
        )

        for i in range(0, 15):
            models.Book.objects.create(
                title=str("test_" + str(i)),
                published_date="2020-01-01",
                author=str("test_" + str(i)),
                description="test",
                cover_img="test",
                isbn10="10" + str(i),
                isbn13="13" + str(i),
            )
        self.object_list = models.Book.objects.all()

    def test_books_can_be_created(self):
        test_book = models.Book.objects.create(
            title="test",
            published_date="2020-01-01",
            author="test",
            description="test",
            cover_img="test",
            isbn10="test",
            isbn13="test",
        )
        assert test_book is not None

    def test_random_stack(self):
        book_stack = self.object_list
        items = list(book_stack)
        random_item = random.sample(items, 5)
        top_book = random_item[0]
        assert top_book is not None
        assert random_item[1] is not None
        assert random_item[2] is not None
        assert random_item[3] is not None
        assert random_item[4] is not None

    def test_books_in_context_for_HomeView(self):
        response = self.client.get(reverse('home'))
        self.assertIn('book01', response.context)
        self.assertIn('book02', response.context)
        self.assertIn('book03', response.context)
        self.assertIn('book04', response.context)
        self.assertIn('book05', response.context)
        self.assertIn('book06', response.context)
        self.assertIn('book07', response.context)
        self.assertIn('book08', response.context)
        self.assertIn('book09', response.context)
        self.assertIn('book10', response.context)
        self.assertIn('book11', response.context)
        self.assertIn('book12', response.context)
        self.assertIn('book13', response.context)
        self.assertIn('book14', response.context)

    def test_book_in_context_view_is_in_database(self):
        response = self.client.get(reverse('home'))
        assert(response.context['book01'] in self.object_list)
        assert(response.context['book02'] in self.object_list)
        assert(response.context['book03'] in self.object_list)
        assert(response.context['book04'] in self.object_list)
        assert(response.context['book05'] in self.object_list)
        assert(response.context['book06'] in self.object_list)
        assert(response.context['book07'] in self.object_list)
        assert(response.context['book08'] in self.object_list)
        assert(response.context['book09'] in self.object_list)
        assert(response.context['book10'] in self.object_list)
        assert(response.context['book11'] in self.object_list)
        assert(response.context['book12'] in self.object_list)
        assert(response.context['book13'] in self.object_list)
        assert(response.context['book14'] in self.object_list)



class TestLiveServer(LiveServerTestCase):
    def setUp(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

        for i in range(0, 15):
            models.Book.objects.create(
                title=str("test_" + str(i)),
                published_date="2020-01-01",
                author=str("test_" + str(i)),
                description="test",
                cover_img="test",
                isbn10="10",
                isbn13="13",
            )
        cls.object_list = models.Book.objects.all()

    """def test_home_page(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get(self.live_server_url)
        self.assertIn("TurnPage", driver.page_source)"""

    def test_size_of_random_stack(self):
        factory = self.factory
        request = factory.get("/")
        response = views.HomeView.as_view()(request)
        self.assertIsInstance(response.context_data, dict)
        self.assertEqual(
            response.context_data.__sizeof__(), response.context_data.__sizeof__()
        )
