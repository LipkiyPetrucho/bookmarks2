from django import forms
from django.forms import Textarea, TextInput

from .models import Image

from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
        }
        widgets = {
            'url': forms.HiddenInput,
            'title': TextInput(attrs={'class': 'form-control form-control-width',
                                      'style': 'background-color: #f8f9fa; border-radius: 5px;',
                                      }),
            'description': Textarea(attrs={'cols': 30,
                                           'rows': 3,
                                           'class': 'form-control form-control-width',
                                           'type': 'text',
                                           'style': 'background-color: #f8f9fa; border-radius: 5px;'
                                           }),
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL не ' \
                                        'соответствует допустимым расширениям изображений.')
        return url

    def save(self, force_insert=False,
                   force_update=False,
                   commit=True):
        # Создание экземпляра изображения: функция вызывает метод save родительского класса
        # (super().save(commit=False)), чтобы создать экземпляр изображения, но еще не сохранять его
        # в базу данных. Параметр commit=False говорит Django, что нужно вернуть объект,
        # но не сохранять его в базу данных.
        image = super().save(commit=False)

        # Получение URL изображения: функция получает URL изображения из очищенных данных
        # формы (self.cleaned_data['url']).
        image_url = self.cleaned_data['url']

        # Создание имени файла: функция создает имя файла изображения, используя функцию slugify
        # для заголовка изображения и добавляет расширение файла, извлеченное из URL изображения.
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # скачать изображение с данного URL-адреса. Функция скачивает изображение, используя
        # библиотеку requests для выполнения HTTP-запроса GET к URL изображения.
        response = requests.get(image_url)

        # Сохранение изображения: функция сохраняет скачанный файл изображения в поле image
        # модели Image, используя метод save Django для файлов, передавая ему объект ContentFile,
        # экземпляр которого заполнен содержимым скачанного файла. Таким
        # путем файл сохраняется в каталог media проекта. Параметр save=False говорит Django,
        # что файл следует сохранить, но избежать сохранения объекта в базе данных.
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)

        # Для того чтобы оставить то же поведение, что и в изначальном методе save() класса ModelForm,
        # форма сохраняется в базе данных только в том случае, если параметр commit равен True
        if commit:
            image.save()
        return image
