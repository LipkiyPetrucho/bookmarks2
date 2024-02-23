from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea, NumberInput, TextInput, Select
from django.utils import timezone

from .models import Game


def validate_date(value):
    if value < timezone.now().date():
        raise ValidationError('Дата не может быть в прошлом.')


def validate_time(value):
    now = timezone.now()
    if value < now.time() or (value == now.time() and now.date() > value.date()):
        raise ValidationError('Время не может быть в прошлом.')


class GameCreateForm(forms.ModelForm):
    date = forms.DateField(label='Дата игры', widget=forms.TextInput(attrs={
        'type': 'date',
        'class': 'form-control form-control-width',
        'style': 'background-color: #f8f9fa; border-radius: 5px;'}),
                           validators=[validate_date])
    time = forms.TimeField(label='Время начала игры', widget=forms.TextInput(attrs={
        'type': 'time',
        'class': 'form-control form-control-width',
        'style': 'background-color: #f8f9fa; border-radius: 5px;'}),
                           validators=[validate_time])

    class Meta:
        model = Game
        fields = ['sport',
                  'place',
                  'amount_players',
                  'price',
                  'description',
                  'date',
                  'time',
                  'duration']
        labels = {
            'sport': 'Вид спорта',
            'place': 'Место игры',
            'amount_players': 'Количество игроков',
            'price': 'Цена игры',
            'description': 'Описание',
            'date': 'Дата игры',
            'time': 'Время начала игры',
            'duration': 'Продолжительность'
        }

        widgets = {
            'sport': Select(attrs={'class': 'form-control form-control-width',
                                            'style': 'background-color: #f8f9fa; border-radius: 5px;',
                                   }),
            'place': TextInput(attrs={'class': 'form-control form-control-width',
                                      'style': 'background-color: #f8f9fa; border-radius: 5px;',
                                      }),
            'amount_players': NumberInput(attrs={'class': 'form-control form-control-width',
                                                 'step': '1',
                                                 'style': 'background-color: #f8f9fa; border-radius: 5px;',
                                                 }),
            'description': Textarea(attrs={'cols': 30,
                                           'rows': 3,
                                           'class': 'form-control form-control-width',
                                           'type': 'text',
                                           'placeholder': 'Опишите например: есть душевые, есть парковочные места',
                                           'aria-label': 'default input example',
                                           'style': 'background-color: #f8f9fa; border-radius: 5px;'
                                           }),
            'price': NumberInput(attrs={'step': '10',
                                        'class': 'form-control form-control-width',
                                        'style': 'background-color: #f8f9fa; border-radius: 5px;'
                                        }),
            'duration': TextInput(attrs={'placeholder': 'HH:MM',
                                         'type': 'time',
                                         'class': 'form-control form-control-width',
                                         'style': 'background-color: #f8f9fa; border-radius: 5px;'}),
        }
