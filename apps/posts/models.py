from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    photo = models.ImageField(upload_to='post_photo')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    def __str__(self):
        return f'Фото - {self.photo}, Автор - {self.author}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комментария"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'Пост - {self.post}, Автор - {self.author}'
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Пост - {self.post}, Автор - {self.user}'
    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

