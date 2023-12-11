
from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    label = models.CharField(max_length=112, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    image = models.ImageField(verbose_name="Фото", upload_to='images', blank=True)
    produced = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def str(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField(verbose_name="Текст")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Публикация")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def str(self):
        return self.content