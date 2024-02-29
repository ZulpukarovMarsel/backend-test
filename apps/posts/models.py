from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

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

# Это функция удаляеть фото из базы данных если пост удаляеться
@receiver(pre_delete, sender=Post)
def delete_post_photo(sender, instance, **kwargs):
    instance.photo.delete()


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

