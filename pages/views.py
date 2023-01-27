from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "home.html"
# when i call HomePage ^ this file will be open in browser

class AboutPage(TemplateView):
    template_name = "about.html"