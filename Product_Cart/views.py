from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Product, Cart, Productincard, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import cardform
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class ProductList(LoginRequiredMixin,ListView):
    template_name = "Product_cart/productlist.html"
    model = Product
    context_object_name = "products"
    # paginate_by = 2



from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
PRODUCT_PER_PAGE = 2

# def ProductList(request):

#     ordering = request.GET.get('ordering', "")
#     search = request.GET.get('search', "")
#     price = request.GET.get('price', "")

    # if search:
    #     product = Product.objects.filter(Q(product_name_icontains=search) | Q(brand_icontains=search))

    # else:
    #     product = Product.objects.all()
    
    # if ordering:
    #     product = Product.order_by(ordering)

    # if price:
    #     product = Product.filter(price__lt=price)

    # product = Product.objects.all

    # page = request.GET.get('page',1)

    # product_paginator = Paginator(product, PRODUCT_PER_PAGE)
    
    # try:
    #     product = product_paginator.page(page)
    
    # except EmptyPage:
    #     product = product_paginator.page(product_paginator.num_pages)
    # except:
    #     product = product_paginator.page(PRODUCT_PER_PAGE)

    # return render(request, "Product_cart/productlist.html", {'product':product, 'page_obj': product, 'is_paginated': True, 'paginator': product_paginator})



class ProductDetails(LoginRequiredMixin,DetailView):
    template_name = "Product_cart/productdetails.html"
    model = Product
    context_object_name = 'product'
    # paginate_by = 2


@login_required
def AddtoCard(request, pk):
    try:
        cart = Cart.objects.get(CustomUser_id = request.user.id)
        try:
            product = Product.objects.get(product_id = pk)
            try:
                productincard = Productincard.objects.get(cart = cart, product = product)
                productincard.quantity = productincard.quantity + 1
                productincard.save()
                messages.success(request, "product added to cart")
                return redirect("displayview")
            except:
                productincard = Productincard.objects.create(cart=cart, product = product, quantity = 1)
                messages.success(request, "product added to cart")
                return redirect("displayview")
        except:
            messages.error(request, "Product can not found")
            return redirect("product_list")
    except:
        
        cart = Cart.objects.create(CustomUser_id = request.user.id)
        try:
                product = Product.objects.get(product_id=pk)
                productincard = Productincard.objects.get(cart = cart, product = product)
                productincard.quantity = productincard.quantity + 1

                productincard.save()
                messages.success(request, "product added to cart")
                return redirect("displayview")
        except:
                messages.error(request, "Erroe in adding to cart, Try again")
                return redirect("product_list")


class displayview(LoginRequiredMixin,ListView):
    template_name = 'Product_cart/productinfo.html'
    model = Productincard
    context_object_name = 'cart'


    def get_queryset(self):
       queryset = Productincard.objects.filter(cart = self.request.user.cart)
       return queryset


class UpdateCart(LoginRequiredMixin,UpdateView):
    model = Productincard
    form_class = cardform
    success_url = reverse_lazy("displayview")


    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 302:
            quantity = int(request.POST.get("quantity"))
            if quantity == 0:
                product_in_cart = self.get_object()
                product_in_cart.delete()
            return response
        else:
            messages.error(request, "Error in quantity")
            return redirect(reverse_lazy("displayview"))


class deletefromcart(LoginRequiredMixin, DeleteView):
    model = Productincard
    success_url = reverse_lazy("displayview")



# def payment(request):
#     if request.method == 'POST':
#         try:
#             cart = Cart.objects.get(user= request.user)
#             product_in_cart = Productincard.objects.filter(cart= cart)
#             final_price = 0

#             if(len(product_in_cart)>0):
#                 order = Order.objects.create(user = request.User, total_number = 0)

#                 for product in product_in_cart:
#                     product_in_order = Prod







    # obj = get_object_or_404(Product, product_id=product_id)
    # name = 'car'
    # obj.product_name = name
    # return HttpResponse('update value {}'.format(obj.product_name))



# def quantities_view (request):

#     quantity = request.GET.get('quantity_view')

#     try:
#         quantity = int(quantity)


#     except (ValueError, TypeError):
#         return HttpResponse("specifies the quantity")
    

#     if quantity:
#             a = Product.product_value_limit(int(quantity))
#             return HttpResponse(f'product quantity {a}',a)

#     return HttpResponse(quantity)