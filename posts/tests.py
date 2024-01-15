from django.test import TestCase
from .models import Post
from http import HTTPStatus


class ModelTestCase(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()
        self.assertEqual(posts.count(), 0)
        # self.assertEqual(posts.count(), 1)

    def test_post_has_string_representaion(self):
        post = Post.objects.create(
            title="title",
            subject="title",
            content="title"
        )

        self.assertEqual(str(post), post.title)


class HomePageTest(TestCase):
    

    def setUp(self):
        post = Post.objects.create(
            title="title",
            subject="title",
            content="title"
        )

        post = Post.objects.create(
            title="title 2",
            subject="subject 2",
            content="content 2"
        ) 

    def test_homepage_return_correct_response(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)