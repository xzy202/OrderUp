from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth import logout

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Action for the default route
from django.http import HttpResponse, Http404, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie
#I Import forms
from OrderUp.forms import ResturantForm , OrderForm
from OrderUp.models import Resturant , Order
# from bubbles.models import Feedback, GameStats, UserStats

# from bubbles.forms import RegistrationForm
# Django transaction system so we can use @transaction.atomic
from django.db import transaction

from datetime import datetime
from django.core import serializers

import random

import json
import sys

def main(request):
    context={}
    resturants = Resturant.objects.all()
    context['resturants'] = resturants

    return render(request,'main.html',context)

def createResturant(request):
    context={};
    context['form']= ResturantForm();
    return render(request,'createResturant.html',context);

def addResturant(request):

    new_resturant = ResturantForm(request.POST, request.FILES)

    if not new_resturant.is_valid():
        return render(request,'createResturant.html',context);

    new_resturant.save()

    return redirect(reverse('main'))

def viewresturant(request,id):
    context={}
    id = id
    resturant = get_object_or_404(Resturant,id = id) 
    context['resturant'] = resturant
    context['orderform'] = OrderForm();

    return render(request,'viewresturant.html',context);


#viewcheckout
def addOrder(request,id):
    print ("add_Order")
    id = id
    context={}
    order = OrderForm(request.POST)
    quantity = request.POST['quantity']
    resturant = get_object_or_404(Resturant,id = id) 
    price = resturant.price
    if not order.is_valid():
    	context['resturant'] = resturant;
    	context['orderform'] = OrderForm();
    	print "invalid order"
        return render(request,'viewresturant.html',context);
    total = int(price) * int(quantity)
    new_order = Order(quantity= quantity, resturant= resturant, timestamp = datetime.now(),ordernumber = "XXX",totalprice=total )
    new_order.save()

    return redirect(reverse('checkout',kwargs={'id':id}))

def placeorder(request,id):
    context={}
    ID = id
    resturant = get_object_or_404(Resturant,id = ID)
    orders = Order.objects.filter(resturant = resturant).order_by("timestamp").reverse()
    order = orders[0]
    random_number = []
  
    for i in range (10):    
      random_number.append( str(random.randrange(0,9,1)))  
    
    random_number = "".join(random_number)
      
    order.ordernumber = random_number
    order.save()

    context['resturant'] = resturant
    context['order'] = order
    return render(request,'confirmOrder.html',context);


def myorder(request,ordernumber):
    ordernumber = ordernumber
    context={}
    order = get_object_or_404(Order,ordernumber = ordernumber)
    context['order'] = order
    return render(request,'myOrder.html',context);

def findmyorder(request):
    if request.method != 'POST':
        context={}
        context['ordernumber']=""
        return render(request,'findmyOrder.html',context);
    print(request.POST)
    ordernumber = request.POST.get('ordernumber', False)
    
    return redirect(reverse('myOrder',kwargs={'ordernumber':ordernumber}))

def editorder(request,id):

    return redirect(reverse('viewresturant',kwargs={'id':id}))


def vieworder(request,id):
    ID = id
    context={}
    resturant = get_object_or_404(Resturant,id = ID)
    orders = Order.objects.filter(resturant = resturant).exclude(ordernumber__contains = "XXX").order_by("timestamp").reverse()
    context['orders'] = orders
    context['resturant'] = resturant
    return render(request,'viewOrder.html',context);


def checkout(request,id):
    context={}
    ID = id
    resturant = get_object_or_404(Resturant,id = ID)
    orders = Order.objects.filter(resturant = resturant).order_by("timestamp").reverse()
    order = orders[0]
    context['resturant'] = resturant
    context['order'] = order
    return render(request,'viewcheckout.html',context);

def get_photo(request, id):
    item = get_object_or_404(Resturant, id = id)

    # Probably don't need this check as form validation requires a picture be uploaded.
    if not item.image:
        raise Http404

    return HttpResponse(item.image)

def login(request):
    context={}
    resturants = Resturant.objects.all()
    context['resturants'] = resturants

    return render(request,'main.html',context)

def getlist(request,id):

    ID = id
    context={}
    resturant = get_object_or_404(Resturant,id = ID)
    orders = Order.objects.filter(resturant = resturant).exclude(ordernumber__contains = "XXX").order_by("timestamp").reverse()

    all_list=[]


    for i in range(0,orders.count()):
        order = orders[i] 
        all_list.append(order)
        
    response_text = serializers.serialize('json', all_list)
    return HttpResponse(response_text, content_type='application/json')

    
