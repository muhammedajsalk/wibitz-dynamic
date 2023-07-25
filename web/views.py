import json

from django.shortcuts import render
from web.models import Customer,Subscribe,Feature,Videoblog,Testimonial,Marketing,Product,Blog,Contact
from django.http import HttpResponse


def index(request):
    customer = Customer.objects.all()
    feature = Feature.objects.all()
    videoblog= Videoblog.objects.all()
    testimonial= Testimonial.objects.all()
    marketing = Marketing.objects.all()
    product = Product.objects.all()
    blog = Blog.objects.all()
    context={
        "customers" : customer,
        "features" : feature,
        "videoblogs" : videoblog,
        "testimonials" : testimonial,
        "marketings" : marketing,
        "products" : product,
        "blogs" : blog
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
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    company = request.POST.get("company")
    company_size = request.POST.get("company_size")
    industry = request.POST.get("industry")
    job_role = request.POST.get("job_role")
    country = request.POST.get("country")
    user_agreement = request.POST.get("user_agreement")
    
    if not Contact.objects.filter(email=email).exists():
        
        Subscribe.objects.create(
          email = email,
          first_name = first_name,
          last_name = last_name,
          company = company,
          company_size = company_size,
          industry = industry,
          job_role = job_role,
          country = country,
          user_agreement = user_agreement
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
