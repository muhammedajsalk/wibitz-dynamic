import json

from django.shortcuts import render,get_object_or_404
from web.models import Customer,Subscribe,Feature,Videoblog,Testimonial,Marketing,Product,Blog,Contact
from django.http import HttpResponse
from web.forms import ContactForm


def index(request):
    customer = Customer.objects.all()
    latest_customer = Customer.objects.all()[:4]
    feature = Feature.objects.all()
    videoblog= Videoblog.objects.all()
    testimonial= Testimonial.objects.all()
    marketing = Marketing.objects.all()
    product = Product.objects.all()
    blog = Blog.objects.all()

    form = ContactForm()

    context={
        "customers" : customer,
        "features" : feature,
        "videoblogs" : videoblog,
        "testimonials" : testimonial,
        "marketings" : marketing,
        "products" : product,
        "blogs" : blog,
        "form" : form,
        "latest_customers" : latest_customer
    }
    return render(request,"index.html",context=context)


def subscribe(request):
    email = request.POST.get("email")
    
    if not Subscribe.objects.filter(email=email).exists():
        
        Subscribe.objects.create(
          email = email
        )

        response_data={
            "status" : "success",
            "title" : "Successfully Registered",
            "message" : "You Subscribed to our newsletter successfully"
        }
    else:
        response_data={
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "You are already member. No need to register again"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def contact(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()
        
        response_data={
            "status" : "success",
            "title" : "Successfully Registered",
            "message" : "You Subscribed to our newsletter successfully"
        }
    else:
        response_data={
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "You are already member. No need to register again"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def product(request,pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    context={
        "product":product
    }
    return render(request,"product.html",context=context)