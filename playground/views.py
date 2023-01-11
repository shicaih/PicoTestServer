from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    # query_set = Product.objects.filter(description__isnull=True)
    # query_set = Customer.objects.filter(email__icontains='.com')
    # query_set = Collection.objects.filter(featured_product__isnull = True)
    # query_set = Product.objects.filter(inventory__lt=10)
    # query_set = Order.objects.filter(customer__id=1)
    # query_set = OrderItem.objects.filter(product__collection__id=3)
    # query_set = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt =20))
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    query_set = Product.objects.order_by('title').reverse()
    return render(request, 'hello.html', {'name': 'Shicai', 'products':list(query_set)})
