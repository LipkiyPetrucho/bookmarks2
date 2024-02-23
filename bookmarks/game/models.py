from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Game(models.Model):
    CHOICES = (
        ('football', 'футбол'),
        ('tennis', 'теннис'),
        ('bowling', 'боулинг'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='games_created',
                             on_delete=models.CASCADE)
    sport = models.CharField(max_length=255, choices=CHOICES)
    amount_players = models.PositiveIntegerField(default=2)
    place = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created = models.DateField(default=timezone.now)
    joined_players = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                            related_name='joined_games',
                                            blank=True)
    slug = models.SlugField(max_length=200,
                            blank=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.sport} {self.date} {self.time} {self.place}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sport, allow_unicode=True) + '-' + slugify(self.date, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('game:detail', args=[self.id,
                                              self.slug]) #эти аргументы берутся из полей модели (см. выше)

    def join_game(self, user):
        """
        Добавляет пользователя к игре.

        Args:
            user: Пользователь, который присоединяется к игре.

        Returns:
            True, если пользователь успешно присоединился к игре, False в противном случае.
        """

        if self.joined_players < self.amount_players:
            self.joined_players.add(user)

        else:
            raise Exception('Превышено максимальное количество игроков для этой игры')
