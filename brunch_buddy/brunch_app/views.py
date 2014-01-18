from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import Http404
#from django.template import RequestContext, loader

from brunch_app.models import Restaurant
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


def index (request):
    bucket_list = Restaurant.objects.order_by('-name')[:10]
    # template = loader.get_template('brunch_app/index.html')
    # context = RequestContext(request, {
    #     'bucket_list': bucket_list,
    # })
    # return HttpResponse(template.render(context))

    context = {'bucket_list': bucket_list}
    return render(request, 'brunch_app/index.html', context)

def detail(request, restaurant_id):
    # try:
    #     restaurant = Restaurant.objects.get(pk=restaurant_id)
    # except Restaurant.DoesNotExist:
    #         raise Http404
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'brunch_app/detail.html', {'restaurant': restaurant})

def add(request):
    
    if request.method == 'POST': # If the form has been submitted...
        
        #Gets post from Form for the restaraunt name and stores it  
        subject = request.POST['Restaraunt']
        print subject
        
        return HttpResponseRedirect('') # Redirect after POST
        
    
    return render(request, 'brunch_app/add.html')