from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.gis.geos import Point
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from travel_app.forms import ProfileUserCreationForm, ListForm, LocationForm, PictureForm
from travel_app.models import List, Location, Picture
from wanderful import settings
# from django.contrib.gis import geos
# from django.contrib.gis import measure
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders import Nominatim


def home(request):
    if request.user.is_authenticated():
        return redirect('profile')
    return render(request, 'home.html')

@login_required()
def profile(request):
    lists = List.objects.filter(profile=request.user)
    locations = Location.objects.filter(lists__profile=request.user)
    data = {'lists': lists, 'locations': locations}
    return render(request, 'profile.html', data)


def register(request):
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you, {} for signing up for our website!'.format(user.username)
            html_content = '<h2>Thanks, {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required()
def list_it(request):
    #list_form = ListForm()
    if request.method == "POST":
        list_form = ListForm(request.POST)

        if list_form.is_valid():
            list = List.objects.create(list_name=list_form.cleaned_data['list_name'],
                                       profile=request.user)
    data = {"list_form": ListForm(),
            "all_list": List.objects.filter(profile=request.user)}

    return render(request, 'lists/list_it.html', data)


@login_required()
def location(request):
    return render_to_response('locations/location.html')
""" location_form = LocationForm()

    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            address = location_form.cleaned_data['address']
            name = location_form.cleaned_data['name']
            geolocator = Nominatim()
            location = geolocator.geocode(address)
            if location:
                latitude, longitude = location.latitude, location.longitude
                added_location = Location.objects.create(geom=Point(longitude, latitude),
                                                         address=address,
                                                         name=name)
                if added_location:
                   redirect('view_location', added_location.id)
    return render(request, 'locations/location.html', {'location_form': location_form,
                                                     'locations': Location.objects.all()})
 """

@login_required()
def edit_location(request, location_id):
    picture_form = PictureForm()

    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        # context['posted'] = picture_form.instance
        if picture_form.is_valid() and picture_form.is_multipart():
            pic = Picture(description=picture_form.cleaned_data['description'],
                          image=picture_form.cleaned_data['picture'],
                          location=Location.objects.get(pk=location_id))
            pic.save()
        return redirect('profile')
    return render(request, 'locations/edit_location.html', {'picture_form': picture_form, 'location_id': location_id})



@login_required()
def view_list(request, list_slug):
    list = List.objects.get(slug_name=list_slug)
    locations = list.location.all()
    location_form = LocationForm()

    if request.POST:
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            address = location_form.cleaned_data['address']
            name = location_form.cleaned_data['name']
            geolocator = Nominatim()
            try:
                location = geolocator.geocode(address)
            except:
                raise "Something went wrong"
            if location:
                latitude, longitude = location.latitude, location.longitude
                added_location = Location.objects.create(geom=Point(longitude, latitude),
                                                         address=address,
                                                         name=name)
                added_location.lists.add(list)
                return redirect('view_location', added_location.id)
    return render(request, 'lists/view_list.html', {'locations': locations,
                                                    'location_form': location_form,
                                                    'list': list})

@login_required()
def edit_list(request, list_slug):
    list = List.objects.get(slug_name=list_slug)
    list_form = ListForm(initial={'list_name': list.list_name})
    if request.method == "POST":
        list_form = ListForm(request.POST)

        if list_form.is_valid():
            list.list_name = list_form.cleaned_data['list_name']
            list.save()
            return redirect('list_it')

    data = {"list_form": list_form,
            "list": list}
    return render(request,'lists/edit_list.html', data)

@login_required()
def view_location(request, location_id):
    location = Location.objects.get(pk=location_id)
    picture_form = PictureForm()
    pictures = Picture.objects.filter(location=location)

    data = {'location': location,
            'picture_form': picture_form,
            'pictures': pictures}
    return render(request, 'locations/view_location.html', data)


@login_required()
def upload_picture(request, location_id):
    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            pic = Picture(description=picture_form.cleaned_data['description'],
                          image=picture_form.cleaned_data['picture'],
                          location=Location.objects.get(pk=location_id))
            pic.save()
        return redirect('view_location', location_id)