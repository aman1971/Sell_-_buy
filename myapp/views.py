from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Myproduct
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def product(request):
    page_obj = myproduct = Myproduct.objects.all()

    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        page_obj = myproduct.filter(name__icontains=product_name)

    paginator = Paginator(page_obj,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'myapp/index.html', context)


#Class based view for above products view [Listview]
# class Productlistview(ListView):
#     model = Myproduct
#     template_name = 'myapp/index.html'
#     context_object_name = 'myproduct'
#     paginate_by = 3


# def product_detail(request,id):
#     product = Myproduct.objects.get(id=id)
#     context = {'product':product}
#     return render(request,'myapp/detail.html',context)

#class based view for above product detail view
class ProductDetailView(DetailView):
    model = Myproduct
    template_name = 'myapp/detail.html'
    context_object_name = 'product'

# @login_required
# def add_product(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         desc = request.POST.get('desc')
#         image = request.FILES['upload']
#         seller_name = request.user
#         product = Myproduct(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
#         product.save()
#     return render(request,'myapp/addproduct.html')

#class based view for creating a product
class ProductCreateView(CreateView):
    model = Myproduct
    fields = ['name','price','desc','image','seller_name']   

def update_product(request,id):
    product = Myproduct.objects.get(id=id)
    context = {'product':product}
    if request.method=='POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/product')
    return render(request,'myapp/updateproduct.html', context)

def delete_product(request,id):
    product = Myproduct.objects.get(id=id)
    context = {
        'product':product,
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/myapp/product')
    return render(request,'myapp/delete.html',context)

def my_listings(request):
    product = Myproduct.objects.filter(seller_name=request.user)
    context = {
        'product':product
    }

    return render(request, 'myapp/mylisting.html',context)