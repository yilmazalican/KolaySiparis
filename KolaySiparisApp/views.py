from django.shortcuts import render
from KolaySiparisApp.models import UserInfo, Menu,Restaurant, Address, Order
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import LoginForm, PaymentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
import random
import json
from datetime import datetime




# Create your views here.
def home(request):
     if request.method == 'POST':
         # create a form instance and populate it with data from the request:
         form = LoginForm(request.POST)

         # check whether it's valid:
         if form.is_valid():
             print "buraya geldim"
             user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
             login(request,user)
             return HttpResponseRedirect('/')

         else:
             print form.errors
             print "form valid degil"

     # if a GET (or any other method) we'll create a blank form
     else:
         print "else geldim"
         print request.method
         form = LoginForm()
     print "buraya geldim"





     disct_list = Restaurant.objects.all().distinct()


     print disct_list
     return render(request, 'home.html', {'form': form, 'dictrict':disct_list})












def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):

      # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid() and len(form.cleaned_data) >=6:
            print "burdayim"
            print "form valid"
            u = User.objects.create_user(username=form.cleaned_data["username"],email=form.cleaned_data["email"],password= form.cleaned_data["password"] )
            u.is_superuser = False
            u.last_name = form.cleaned_data["lastname"]
            u.first_name = form.cleaned_data["firstname"]
            u.save()
            userinf = UserInfo()
            userinf.user = u
            userinf.phone = form.cleaned_data["phone"]

            userinf.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            login(request,user)
            return HttpResponseRedirect('/login/')

        else:
            print form.errors
            print "form valid degil"

    # if a GET (or any other method) we'll create a blank form
    else:
        print "else geldim"
        print request.method
        form = RegisterForm()

    print "buraya geldim"
    return render(request, 'register.html', {'form': form})


def restaurant_login_view(request):
    return render(request, 'restaurant_login.html')


def login_view(request):
    return render(request, 'login_view.html')

def customerRestaurant_view(request,res_id):

    ident_menu_res = Menu.objects.filter(restaurant_id=res_id)
    ident_res = Restaurant.objects.get(id=res_id)
    request.session['res_id'] = res_id

    print request.session['res_id']


    return render(request, 'customerRestaurant.html', {'result': ident_menu_res, 'aboutres': ident_res})


def payment(request):

    orders = request.session['orders']
    orders = json.loads(orders)
    orders_list = []
    i = 0
    res_id = request.session['res_id']
    for a in orders:
        i= i+ 1
        b = Menu.objects.get(id=a)
        orders_list.insert(i,b)


    if request.method == 'POST':
         # create a form instance and populate it with data from the request:
         form = PaymentForm(request.POST)

         # check whether it's valid:
         if form.is_valid():
             order = Order()
             print res_id
             order.restaurant_id = res_id
             order.seen=False
             order.payment_type=form.cleaned_data["payment_type"]
             order.customer_id=request.user.id
             order.totalprice=100
             order.status=True
             order.time=datetime.now()
             order.save()

             for p in orders_list:

                 order.menu.add(order.id,p)




         else:
             print form.errors
             print "form valid degil"
         print "success"

     # if a GET (or any other method) we'll create a blank form
    else:
         print "else geldim"
         print request.method
         form = PaymentForm()
    print "buraya geldim"











    ident_adress = Address.objects.filter(user__id=request.user.id)







    return render(request, 'payment.html', {'list': orders_list, 'adress_list': ident_adress, 'form':form})

def editmenu(request):
    return render(request, 'EditMenu.html')

def restaurantlist_view(request, district_name,food_name):


    ident_restaurant2 = Restaurant.objects.filter(menu__name=food_name,district=district_name)

    ident_restaurant = Restaurant.objects.filter(menu__name=food_name,district=district_name).values_list('id',flat=True)
    ident_menu = Menu.objects.filter(restaurant_id__in=ident_restaurant, name=food_name)

    liste = zip(ident_restaurant2,ident_menu)





    return render(request, 'RestaurantList.html', {'result': liste})





def successorder_view(request):
    print(request.is_ajax())
    a = request.POST.get('tasks[]')
    request.session['orders'] = a

    return render(request, 'successorder.html')
