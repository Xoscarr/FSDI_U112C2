from django.test import TestCase
from .models import Post 
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="A test", body="Test")
    
    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.body}"
        self.assertEqual(expected_object_name, "Test")
    
    def test_post_string_representation(self):
        post = Post.objects.get(id=1)
        str_repr = str(post)
        self.assertEqual(str_repr, "A test")

class PostViewTest(TestCase): 
    def setUp(self):
        Post.objects.create(title="Another test", body="Test2")

    def test_listview_url_exists_at_proper_location(self):
        resp = self.client.get("/posts/")
        self.assertEqual(resp.status_code, 200)
    
    def test_listview_url_by_name(self):
        resp = self.client.get(reverse("posts_list"))
        self.assertEqual(resp.status_code, 200)

    def test_listview_uses_correct_template(self):
        resp = self.client.get("/posts/")
        self.assertTemplateUsed(resp, "post_list.html")

    def test_listview_contains_content(self):
        resp = self.client.get(reverse("posts_list"))
        self.assertContains(resp, "Another test")
    
    def test_detailview_exists_at_proper_location(self):
        resp = self.client.get("/posts/1/")
        self.assertEqual(resp.status_code, 200)

    def test_detailview_uses_correct_template(self):
        resp = self.client.get(reverse("post_detail", args=[1]))
        self.assertTemplateUsed(resp, "post_detail.html")

    def test_detailview_contains_content(self):
        resp = self.client.get(reverse("post_detail", args=[1]))
        self.assertContains(resp, "Another test")