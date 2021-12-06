from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from product.models import *
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def index(request):
    setting = Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    testimo = Testimonial.objects.all()
    category = Category.objects.all()[:3]
    offer = Product.objects.get(offer=True)
    banner = Product.objects.get(offer=True)
    featured = Product.objects.filter(featured=True)
    latest = Product.objects.filter(latest=True)

    context={
        'setting':setting,
        'brands': brands,
        'banner':banner,
        'testimo': testimo,
        'category':category,
        'offer': offer,
        'featured': featured,
        'latest': latest
    }

    return render(request, 'index.html', context)
    # return HttpResponse('Converting Our Ecommerce template into an App')


def about(request):
    setting = Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    testimo = Testimonial.objects.all()
    category = Category.objects.all()

    context = { 
        'setting': setting,
        'brands': brands,
        'testimo': testimo,
        'category': category,
    }          
    # return HttpResponse('About page created')
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team will reach you soon.")
            return redirect('/contact')


    setting = Setting.objects.get(pk=1)
    form = ContactForm
    brands = Brand.objects.all()
    category = Category.objects.all()
       
    context= { 'setting': setting,
                'form': form,
                'brands': brands,
                'category': category,                
    }

    return render(request, 'contact.html', context)


def category(request):
    setting= Setting.objects.get(pk=1)
    brands = Brand.objects.all()
    offer = Product.objects.get(offer=True)
    category = Category.objects.order_by('-created_at').filter(status=True)
    paginator = Paginator(category,4)
    page= request.GET.get('page')
    paged_category = paginator.get_page(page)
    
    context= {
            'setting': setting,
            'brands': brands,
            'offer': offer,
            'category': paged_category,
    }

    return render(request, 'categories.html', context)

def product_list(request,id,slug):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata= Category.objects.get(pk=id)
    products = Product.objects.filter(category__id=id)
    paginator = Paginator(products,2)
    page= request.GET.get('page')
    paged_products = paginator.get_page(page)
    

    context= {
                'setting': setting,
                'category': category,
                'catdata': catdata,
                'products': paged_products,
    }

    return render(request, 'products.html', context)
    # return HttpResponse(products)



def prod_detail(request,id,slug):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)

    
    context= {
                'setting': setting,
                'category': category,
                'products': products,
                'product': product,
                'images': images,
    }

    return render(request, 'product-details.html', context)