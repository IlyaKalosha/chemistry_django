from django.views.generic import TemplateView


class HealthCheckView(TemplateView):
    template_name = "healthcheck.html"

