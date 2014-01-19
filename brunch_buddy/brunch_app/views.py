from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import Http404
#from django.template import RequestContext, loader

from brunch_app.models import Restaurant
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


def index (request):
    bucket_list = Restaurant.objects.order_by('-name')[:20]

    context = {'bucket_list': bucket_list}
    return render(request, 'brunch_app/index.html', context)


def detail(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST': # If the form has been submitted...
        
        restaurant.delete()
        return HttpResponseRedirect('../../brunch_app/') # Redirect after POST
    return render(request, 'brunch_app/detail.html', {'restaurant': restaurant})


def add(request):

    return render(request, 'brunch_app/add.html')


def confirm (request):
#def confirm (request):
    if request.method=="POST":

        print request.POST['Restaurant']
    
        #initialize choices array
        choices = []
        #add entered restaurant to choices
        restaurant = Restaurant(name=request.POST['Restaurant'], location="Junk", status=False)
        #add now unsaved restaurant to choices array
        choices.append(restaurant)

        #make call to Yelp API
        #grab top x
        #pass back to view for client decision

        context = {'choices': choices}
        return render(request, 'brunch_app/confirm.html', context)

    return HttpResponseRedirect('../../brunch_app')

def edit(request, restaurant_id):
   
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST': 
        #Grabs info from edit page and saves it in the current restaurant instance
        name = request.POST['Restaurant Name']
        location = request.POST['Restaurant Location']
        status = request.POST.has_key('Restaurant Status')

        restaurant.name = name
        restaurant.location = location
        restaurant.status = status

        restaurant.save()
        
        return HttpResponseRedirect('../../brunch_app/') # Redirect after POST
    return render(request, 'brunch_app/edit.html', {'restaurant': restaurant})

def confirmPart2 (request):

    data = request.POST['choice']
    attributes = data.split(',')
    restaurant = Restaurant(name=attributes[0], location=attributes[1], status=False)
    if (attributes[2]=='True'):
        restaurant.status=True
    restaurant.save()
    return HttpResponseRedirect('../../brunch_app/') # Redirect after POST

