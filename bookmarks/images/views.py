from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        # форма отправлена
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # данные в форме валидны.
            # cd - это переменная, которая содержит „очищенные” данные формы, то есть данные,
            # которые были проверены на валидность.
            cd = form.cleaned_data
            new_image = form.save(commit=False)

            # назначить текущего пользователя элементу. В новый экземпляр изображения добавляется
            # связь с текущим пользователем, который выполняет запрос. Так
            # мы будем знать, кто закачивал каждое изображение.
            # В Django, request.user представляет текущего авторизованного пользователя.
            new_image.user = request.user
            new_image.save()
            messages.success(request,
                             'Изображение успешно добавлено')
            # перенаправить к представлению детальной информации о только что созданном элементе
            return redirect(new_image.get_absolute_url())
    else:
        # скомпоновать форму с данными,
        # предоставленными буркмарклетом методом GET
        form = ImageCreateForm(data=request.GET)

    # эта строка кода говорит Django отрендерить шаблон 'images/image/create.html' с контекстом,
    # который содержит форму и секцию. render - это функция Django,
    # которая объединяет шаблон с контекстом и возвращает HTTP-ответ.
    # В данном случае, контекст - это словарь {'section': 'images', 'form': form}, который передается
    # в шаблон. В шаблоне вы можете получить доступ к этим переменным как {{ section }} и {{ form }}.
    # Это позволяет вам динамически изменять содержимое HTML на основе данных формы и секции.
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})
