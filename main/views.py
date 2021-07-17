"""Required Django Modules"""
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Ratings

def homepage(request):
    """ homepage view """
    item_per_page = 20
    param_val = request.GET.get("your_param")
    if param_val is not None:
        with open('/var/www/topcoder/data.txt', 'w') as file:
            data = file.write(param_val)
    with open('/var/www/topcoder/data.txt', 'r') as file:
        data = file.read()
    param_input_value = request.POST.get("your_name")
    ordered = Ratings.objects.all()[:400]
    if param_input_value:
        item_per_page = 500
        param_input_value = (str(param_input_value)).strip()
        if data == "name":
            ordered = Ratings.objects.filter(name__icontains=f'{param_input_value}')
        elif data == "country":
            ordered = Ratings.objects.filter(country__icontains=f'{param_input_value}')
        elif data == "organization":
            ordered = Ratings.objects.filter(organization__icontains=f'{param_input_value}')
        elif data == "username":
            ordered = Ratings.objects.filter(username__istartswith=f'{param_input_value}')
        elif data == "city":
            ordered = Ratings.objects.filter(city__icontains=f'{param_input_value}')
    else:
        ordered = Ratings.objects.all()[:400]
    if request.GET.get('order_by'):
        order_by = request.GET.get('order_by', 'leaderboard_rank')
        ordered = Ratings.objects.all().order_by(order_by)[:400]
        messages.success(request, f"Table Ordered by {order_by}")
    page = request.GET.get('page', 1)
    paginator = Paginator(ordered, item_per_page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    out_dict = {"users": users}
    return render(request=request, template_name="main/index.html", context=out_dict)
