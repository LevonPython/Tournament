from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class TournamentForm(forms.Form):
    name = forms.CharField(label='Tournament Name')
    player1 = forms.CharField()
    player2 = forms.CharField()
    player3 = forms.CharField()
    player4 = forms.CharField()
    player5 = forms.CharField()
    player6 = forms.CharField()
    player7 = forms.CharField()
    player8 = forms.CharField()

class MatchForms(forms.Form):
    player1 = forms.CharField(max_length=30)
    player2 = forms.CharField(max_length=30)
    score1 = forms.IntegerField()
    score2 = forms.IntegerField()