from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
#def homePageView(request):
#	return HttpResponse("Hello Agnes")




#def payment_form(request):

 #   context = { "stripe_key": settings.STRIPE_PUBLIC_KEY }
  #  return render(request, "yourtemplate.html", context)


class HomePageView(TemplateView):

	template_name='pages/index.html'

class AboutPageView(TemplateView):

	template_name='pages/about.html'

class CategoryView(TemplateView):

	template_name='pages/category.html'


class ContactView(TemplateView):

	template_name='pages/contact.html'


class AudioView(TemplateView):

	template_name='pages/single-audio.html'



class GalleryView(TemplateView):

	template_name='pages/single-gallery.html'

class StandardView(TemplateView):

	template_name='pages/standard.html'

class VideoView(TemplateView):

	template_name='pages/single-video.html'
class GuideView(TemplateView):

	template_name='pages/style-guide.html'
class LoginView(TemplateView):
	template_name='pages/login.html'

class SignUpView(TemplateView):
	

	template_name='pages/signup.html'
class MappingView(TemplateView):
	template_name='pages/mapping.html'
