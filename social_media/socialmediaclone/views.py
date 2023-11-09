from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'about_us.html'
class TestPage(TemplateView):
    template_name = 'logged_in.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

