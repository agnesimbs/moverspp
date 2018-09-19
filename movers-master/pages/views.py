from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
import pymysql
connection=pymysql.connect(host="localhost",user="root",password="",database="movers")
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
def loginHandler(request):
	username=request.POST.get("username")
	password=request.POST.get("password")
	cursor=connection.cursor()
	cursor.execute("SELECT name,password FROM registration")
	for (n,p) in cursor:
		if username==n and password==p:
			# render(request,'pages/login.html',{})
			cursor.close()
			return redirect("/booking/")
	cursor.close()
	return redirect("/login/")

def bookinghandler(request):
	name=request.POST.get("name")
	pickup=request.POST.get("pickup")
	drop=request.POST.get("drop")
	time=request.POST.get("time")
	date=request.POST.get("date")
	phone=request.POST.get("phone")
	cursor=connection.cursor()
	cursor.execute("INSERT INTO book(name,number,pickup,droplocation,date,time)VALUES('{}','{}','{}','{}','{}','{}')".format(name,phone,pickup,drop,date,time))
	connection.commit()
	cursor.close()

	return redirect("/index/")


	
	
		

class SignUpView(TemplateView):
	

	template_name='pages/signup.html'
class MappingView(TemplateView):
	template_name='pages/mapping.html'
	
class BookingView(TemplateView):
	template_name='pages/booking.html'
