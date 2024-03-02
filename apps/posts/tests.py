from apps.posts.models import Post, Comment, Like
from apps.user.models import User
from django.test import TestCase


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )

    def test_create_post(self):
        post = Post.objects.create(
            photo='C:\\Users\\User\\Pictures\\обои\\photo_2024-02-16_20-40-50.jpg',
            description='Test post',
            author=self.user
        )

        self.assertEqual(post.photo, 'C:\\Users\\User\\Pictures\\обои\\photo_2024-02-16_20-40-50.jpg')
        self.assertEqual(post.description, 'Test post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(Post.objects.count(), 1)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.post = Post.objects.create(
            photo='C:\\Users\\User\\Pictures\\обои\\photo_2024-02-16_20-40-50.jpg',
            description='Test post',
            author=self.user
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            post=self.post,
            text='Test comment',
            author=self.user
        )

        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.text, 'Test comment')
        self.assertIsNotNone(comment.created_at)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(Comment.objects.count(), 1)

class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.post = Post.objects.create(
            photo='C:\\Users\\User\\Pictures\\обои\\photo_2024-02-16_20-40-50.jpg',
            description='Test post',
            author=self.user
        )

    def test_create_like(self):
        like = Like.objects.create(
            post=self.post,
            user=self.user
        )

        self.assertEqual(like.post, self.post)
        self.assertEqual(like.user, self.user)
        self.assertEqual(Like.objects.count(), 1)

