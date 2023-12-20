from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ApplicationUser


class ApplicationUserCreationForm(UserCreationForm):

    class Meta:
        model = ApplicationUser
        fields = ('email', 'password')


class ApplicationUserChangeForm(UserChangeForm):

    class Meta:
        model = ApplicationUser
        fields = ('email', 'password')
