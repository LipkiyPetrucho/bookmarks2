from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import GameCreateForm
from .models import Game


@login_required
def game_create(request):
    if request.method == 'POST':
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_game = form.save(commit=False)
            new_game.user = request.user
            new_game.save()
            messages.success(request,
                             'Игра успешно создана')
            return redirect(new_game.get_absolute_url())
    else:
        form = GameCreateForm(data=request.GET)
    return render(request,
                  'games/game/create.html',
                  {'section': 'games',
                   'form': form})


def game_detail(request, id, slug):
    game = get_object_or_404(Game, id=id, slug=slug)
    return render(request,
                  'games/game/detail.html',
                  {'section': 'games',
                   'game': game})
