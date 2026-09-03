"""Define URL patterns for users."""
from django.urls import path
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse

from . import views

app_name = 'users'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('learning_logs:topics'))
        return super().dispatch(request, *args, **kwargs)


urlpatterns = [
    # Login Page
    path('login/', CustomLoginView.as_view(), name='login'),
    # Logout Page
    path('logout/', views.logout_view, name='logout'),
    # Registration Page
    path('register/', views.register, name='register'),
]
