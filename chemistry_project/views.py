from django.views.generic import TemplateView
from django.contrib.auth.models import User


class HealthCheckView(TemplateView):
    template_name = "healthcheck.html"

