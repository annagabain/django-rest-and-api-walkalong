# from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='anna', password='pass')

    def test_can_list_posts(self):
        anna = User.objects.get(username='anna')
        Post.objects.create(owner=anna, title='some title')
        response = self.client.get('/posts/')
        # deliberately failed
        # self.assertEqual(response.status_code, status.HTTP_200_CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('=============================')
        print('response data: ', response.data)
        print('response data length (is a single post):', len(response.data))
    
    def test_logged_in_user_can_create_post(self):
        self.client.login(username='anna', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        # deliberately failed
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_post(self):
        response = self.client.post('/posts/')
        # deliberately failed
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
