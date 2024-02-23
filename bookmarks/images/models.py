from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_like',
                                       blank=True)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображений'
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id,
                                              self.slug]) #эти аргументы берутся из полей модели (см. выше)
