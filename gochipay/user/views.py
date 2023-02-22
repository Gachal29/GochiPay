from django.views.generic import TemplateView


class ReadView(TemplateView):
    template_name = "read.html"
