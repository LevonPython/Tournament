from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import TournamentModel
from .forms import TournamentForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def add_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            tour_model = TournamentModel()
            tour_model.user = request.user
            tour_model.name = form.cleaned_data['name']
            tour_model.player1 = form.cleaned_data['player1']
            tour_model.player2 = form.cleaned_data['player2']
            tour_model.player3 = form.cleaned_data['player3']
            tour_model.player4 = form.cleaned_data['player4']
            tour_model.player5 = form.cleaned_data['player5']
            tour_model.player6 = form.cleaned_data['player6']
            tour_model.player7 = form.cleaned_data['player7']
            tour_model.player8 = form.cleaned_data['player8']

            tour_model.save()
            return redirect('profile')
    else:
        form = TournamentForm()
    return render(request, 'users/add_tournament.html', {'form': form})


def change_tournament(request, tournament_name_slug=None):
    return render(request, 'matches_tour/change_tour.html')


def show_tournament(request, tournament_name_slug=None):
    tour = TournamentModel.objects.get(slug=tournament_name_slug)
    print('\n', tour.slug, '\n')
    return render(request, 'matches_tour/show_tournament.html', {'tour': tour})


def match(request, tournament_name_slug=None):
    return render(request, 'matches_tour/match.html')


def add_match(request, tournament_name_slug=None):
    tour = TournamentModel.objects.get(slug=tournament_name_slug)
    return render(request, 'matches_tour/add_match.html', {'tour': tour})