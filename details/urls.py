from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView

from details.views import signup, login, home
from details.views import profile_view


urlpatterns = [
    url(r'^$', profile_view, name='profile_page'),
    url(r'^account/$', home, name='home_page'),
    url(r'^signup/', signup, name='signup_page'),
    url(r'^login$', LoginView.as_view(
        template_name="details/login_page.html"), name='login_page'),
    url(r'logout$', LogoutView.as_view(), name='logout_page'),
]
