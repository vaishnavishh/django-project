from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Enrollment

# 1. The Login View
class CustomLoginView(LoginView):
    template_name = 'core/login.html' # We will create this HTML file next!

# 2. The Dashboard View
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html' # We will create this one next too!

    # This function grabs the specific data for the logged-in user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch only the enrollments that belong to the user who is currently logged in
        context['enrollments'] = Enrollment.objects.filter(user=self.request.user)
        return context
