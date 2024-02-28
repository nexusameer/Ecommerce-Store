from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User


# Create your views here.

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("There was an error in logging in, try again"))
            return redirect('loginuser')
    else:
        return render(request, 'loginuser.html')


def logoutuser(request):
    logout(request)
    return redirect('index')


def registeruser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Use 'password1' field
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    context = {'form': form}
    return render(request, 'registeruser.html', context)


def index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'product': product,
        'category': category,
        'brand': brand
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html')


def shop_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'product': product,
        'category': category,
        'brand': brand
    }
    return render(request, 'shop.html', context)


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        user = request.user

        print(address, phone, pincode, cart, user)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b
            print(i)
            order = Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                pincode=pincode,
                phone=phone,
                total=total
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')
    return render(request, 'checkout.html')


def yourorder(request):
    user = request.user
    order = Order.objects.filter(user=user)

    context = {
        'order': order
    }
    return render(request, 'yourorder.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')


# add to cart
@login_required(login_url="/loginuser")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    next_url = request.GET.get('product')

    if next_url:
        return redirect("product")
    else:
        return redirect("index")


@login_required(login_url="/loginuser/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cartdetails")


@login_required(login_url="/loginuser/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cartdetails")


@login_required(login_url="/loginuser/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cartdetails")


@login_required(login_url="/loginuser/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cartdetails")


@login_required(login_url="/loginuser/")
def cartdetails(request):
    return render(request, 'cartdetails.html')
