from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'date_': datetime.today()}


class Login(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized_page.html'
    login_url = '/admin'
