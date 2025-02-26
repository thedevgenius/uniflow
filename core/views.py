from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            try:
                send_mail('Test Mail', 'Hello', settings.EMAIL_HOST_USER, [email])
            except Exception as e:
                print(e)
        else:
            print('Fill the field')
        return render(request, self.template_name)