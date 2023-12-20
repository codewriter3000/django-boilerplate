from django.views import generic
from .models import ApplicationUser as User


# Create your views here.
class UserList(generic.ListView):
    queryset = User.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = super().get_queryset()
        return context


class UserDetail(generic.DetailView):
    model = User
    template_name = 'profile.html'
