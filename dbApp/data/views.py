from django.shortcuts import render, redirect
from .forms import UserForm, ClientForm, RegularUserForm, ProUserForm, PageForm, RecordForm, ReviewForm, DiseaseForm, EventForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from . models import *
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    events = Event.objects.filter(client=request.user)
    context = {'event_list': events}
    return render(request, 'data/dashboard.html', context)

@login_required
def event_detail(request, id):
    event = get_object_or_404(Event, pk=id)
    if event.client == request.user:
        return render(request, 'data/event_detail.html', {'event': event})
    else:
        raise PermissionDenied

# def edit_event(request, event_id):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return register(request)
#         else:
#             print form.errors
#     else:
#         form = EventForm()
#     return render(request, 'data/add_event.html', {'form': form})

@login_required
def record_detail(request, id):
    record = get_object_or_404(Record, pk=id)
    if record.event.client == request.user:
        return render(request, 'data/record_detail.html', {'record': record})
    else:
        raise PermissionDenied

@login_required
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print (form.errors)
    else:
        form = PageForm()
    return render(request, 'data/add_page.html', {'form': form})

def page_detail(request, id):
    page = get_object_or_404(Page, pk=id)
    return render(request, 'data/page_detail.html', {'page': page})

def page_list(request):
    pages = Page.objects.order_by('name')
    return render(request, 'data/page_list.html', {'pages': pages})

@login_required
def add_disease(request):
    if not request.user.client.pro :
        raise PermissionDenied
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print (form.errors)
    else:
        form = DiseaseForm()
    return render(request, 'data/add_disease.html', {'form': form})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        form.save(commit=True)
        form.client = request.user
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print (form.errors)
    else:
        form = EventForm()
    return render(request, 'data/add_event.html', {'form': form})

@login_required
def edit_event(request, id):
    event = get_object_or_404(Event, pk=id)
    if event.client != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print (form.errors)
    else:
        form = EventForm()
    return render(request, 'data/add_event.html', {'form': form})

@login_required
def add_record(request, id=None, event_id=None):
    if id:
        record = get_object_or_404(Record, pk=id)
        if record.event.client != request.user:
            raise PermissionDenied
    else:
        record = None
    if request.method == 'POST':
        if id:
            form = RecordForm(request.POST, instance=record)
        else:
            form = RecordForm(request.POST)
        form.save(commit=False)
        if event_id:
            event = get_object_or_404(Event, pk=event_id)
            form.event = event
        else :
            raise PermissionDenied
        if form.is_valid():
            form.save()
            return register(request)
        else:
            print (form.errors)
    else:
        if id:
            form = RecordForm(instance=record)
        else:
            form = RecordForm()
    return render(request, 'data/add_record.html', {'form': form})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print (form.errors)
    else:
        form = ReviewForm()
    return render(request, 'data/add_review.html', {'form': form})


def register(request):
    registered = False
    if request.method == 'POST':
        regular_form = RegularUserForm()
        pro_form = ProUserForm()
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)
        if user_form.is_valid() and client_form.is_valid():
            client = client_form.save(commit=False)
            if client.pro == True:
                pro_form = ProUserForm(data=request.POST)
                extra_form = pro_form
            else:
                regular_form = RegularUserForm(data=request.POST)
                extra_form = regular_form
            if extra_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                client.user = user
                if 'pic' in request.FILES:
                    client.pic = request.FILES['pic']
                client.save()
                myuser = extra_form.save(commit=False)
                myuser.client = client
                myuser.save()
                registered = True
            else:
                print (extra_form.errors)
        else:
            print (user_form.errors)
            print (client_form.errors)
    else:
        if not request.user.is_authenticated:
            user_form = UserForm()
            client_form = ClientForm()
            pro_form = ProUserForm()
            regular_form = RegularUserForm()
        else:
            redirect('/dashboard')
    return render(request,
            'data/register.html',
            {'user_form': user_form, 'client_form': client_form, 'pro_form': pro_form, 'regular_form': regular_form, 'registered': registered} )




def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/data/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'data/login.html', {})


# def ajax_login(request):

#     if request.method == 'POST':
#         data = {}
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if (not user is None) and (user.is_active):
#             login(request, user)
#             if not request.POST.get('rem', None):
#                 request.session.set_expiry(0)
#             data['success'] = "You have been successfully Logged In"
#         else:
#             data['error'] = "There was an error logging you in. Please Try again"
#         return JsonResponse(data)
#     else:
#         return render(request, 'data/login.html', {})