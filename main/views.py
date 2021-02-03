from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Ratings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
  
  


def homepage(request): 
    item_per_page =20
     
    t= request.GET.get("your_param")
    if t != None:

        with open('/var/www/topcoder/data.txt', 'w') as file:
        
            data = file.write(t) 

    with open('/var/www/topcoder/data.txt', 'r') as file:
    
        data = file.read()
 
    x= request.POST.get("your_name")
    
    ordered = Ratings.objects.all()[:400]
    if x : 
        print(data,x)
        item_per_page=500
        
        if data == "name":
        
            ordered =  Ratings.objects.filter(name__icontains=f'{x}')
        elif data == "country":
            ordered =  Ratings.objects.filter(country__icontains=f'{x}')
        
        elif data =="organization":
            ordered =  Ratings.objects.filter(organization__icontains=f'{x}')
    
        if  data =="username":
         ordered =  Ratings.objects.filter(username__istartswith=f'{x}')
        
        elif  data =="city":
            ordered =  Ratings.objects.filter(city__icontains=f'{x}')
    else:
        ordered = Ratings.objects.all()[:400]
            
         
    if request.GET.get('order_by'):
        order_by = request.GET.get('order_by','leaderboard_rank')
        ordered = Ratings.objects.all().order_by(order_by)[:400]
        messages.success(request,f"Table Ordered by {order_by}")
    
    
    
    page = request.GET.get('page', 1)
    paginator = Paginator(ordered, item_per_page)
    try:
        users = paginator.page(page)    
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    
        

    x={"users":users}
    
    return render(request=request,template_name="main/index.html",context=x)



