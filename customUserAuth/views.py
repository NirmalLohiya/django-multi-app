from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy



class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'customuserauth/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'   #in cas the your neww appname like customeruserauth so chnage /cutomeruserauth/login and main app setting ass some setting
    http_method_names = ['get', 'post']  # Allow GET logout



class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'customuserauth/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile_view(request):
    return render(request, 'customuserauth/profile.html', {'user': request.user})





class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'customUserAuth/password_change.html'
    success_url = reverse_lazy('login')  # Redirect to login page after success

    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)  # Force logout after password change
        return redirect(self.get_success_url())  # Redirect to login

    def form_invalid(self, form):
        # If there's an error, stay on the same page and show the form
        return self.render_to_response(self.get_context_data(form=form))