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
    if request.method == 'POST': # If the form has been submitted...
        
        restaurant.delete()
        return HttpResponseRedirect('../../brunch_app/') # Redirect after POST
    return render(request, 'brunch_app/detail.html', {'restaurant': restaurant})

def add(request):
    
    if request.method == 'POST': 

        subject = request.POST['Restaraunt']

        restaurant = Restaurant(name=subject, location="Junk", status=False)

        restaurant.save()
        

        return HttpResponseRedirect('../brunch_app/') # Redirect after POST
    
    return render(request, 'brunch_app/add.html')

<<<<<<< HEAD

def confirm(request, restaurant_id):
    #initialize choices array
    choices = []
    #This restaurant was entered via add view
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    choices.add(restaurant)

    #call the yelp API and search for restaurant

    #grab top 5 to present to user

    #pass 5 suggestions to the client to chooose
    return render(request, 'brunch_app/confirm.html, {'choices':choices)
=======
def edit(request, restaurant_id):
   
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST': 
        #Grabs info from edit page and saves it in the current restaurant instance
        name = request.POST['Restaurant Name']
        location = request.POST['Restaurant Location']
        status = request.POST['Restaurant Status']

        restaurant.name = name
        restaurant.location = location
        restaurant.status = status

        restaurant.save()
        

        return HttpResponseRedirect('../../brunch_app/') # Redirect after POST
    return render(request, 'brunch_app/edit.html', {'restaurant': restaurant})
>>>>>>> c890a25d795f5f2249acafcbbfc5d68d61da0ce2
