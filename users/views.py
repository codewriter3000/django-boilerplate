from django import urls
from django.contrib.auth import views, login as auth_login
from django.views import generic

from .models import ApplicationUser as User


# Create your views here.
class UserList(generic.ListView):
    queryset = User.objects.all()
    template_name = 'index.html'
    context_object_name = 'user_list'


class UserDetail(generic.DetailView):
    model = User
    template_name = 'profile.html'


class UserCreate(generic.CreateView):
    model = User
    template_name = 'create.html'
    fields = ('email', 'password')


class UserLogin(views.LoginView):
    template_name = 'login.html'

    # def form_valid(self, form):
    #     auth_login(self.request, form.get_user())
    #     return urls.reverse('user_detail', kwargs={"pk": form.get_user().pk})


class UserLogout(views.LogoutView):
    pass
