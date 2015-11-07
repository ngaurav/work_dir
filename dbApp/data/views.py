from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ClientForm, RegularUserForm, ProUserForm, PageForm, PageContactForm, RecordForm, ReviewForm, DiseaseForm, EventForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from . models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'data/logout.html', {})

@login_required
def dashboard(request):
    client = get_object_or_404(Client, pk=request.user.id)
    if client.pro:
        pro_user = get_object_or_404(ProUser, client=client)
        disease_list = Disease.objects.all()
        return render(request, 'data/dashboard2.html',{'disease_list': disease_list, 'page':pro_user.page})
    else:
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

# @login_required
# def record_detail(request, id):
#     record = get_object_or_404(Record, pk=id)
#     if record.event.client == request.user:
#         return render(request, 'data/record_detail.html', {'record': record})
#     else:
#         raise PermissionDenied

@login_required
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            if 'image' in request.FILES:
                page.image = request.FILES['image']
            page.save()
            return redirect('/page')
        else:
            print (form.errors)
    else:
        form = PageForm()
    return render(request, 'data/add_page.html', {'form': form})

@login_required
def edit_page_contact(request, id):
    page = get_object_or_404(Page, pk=id)
    if not page.verified:
        raise PermissionDenied
    pro_user = get_object_or_404(ProUser, page=page)
    if pro_user.client.user != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = PageContactForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            if 'image' in request.FILES:
                page.image = request.FILES['image']
            page.save()
            return redirect('/')
        else:
            print (form.errors)
    else:
        form = PageContactForm(instance=page)
    return render(request, 'data/add_page.html', {'form': form})

@login_required
def edit_disease(request, id):
    client = get_object_or_404(Client, pk=request.user.id)
    if not client.pro:
        raise PermissionDenied
    disease = get_object_or_404(Disease, pk=id)
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print (form.errors)
    else:
        form = DiseaseForm(instance=disease)
    return render(request, 'data/add_disease.html', {'form': form})

@login_required
def add_disease(request):
    client = get_object_or_404(Client, pk=request.user.id)
    if not client.pro:
        raise PermissionDenied
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print (form.errors)
    else:
        form = DiseaseForm()
    return render(request, 'data/add_disease.html', {'form': form})

def page_detail(request, id):
    page = get_object_or_404(Page, pk=id)
    return render(request, 'data/page_detail.html', {'page': page})

def page_list(request):
    pages = Page.objects.order_by('name')
    return render(request, 'data/page_list.html', {'pages': pages})

@login_required
def add_event(request):
    client = get_object_or_404(Client, pk=request.user.id)
    if client.pro:
        raise PermissionDenied
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.client = request.user
            event.save()
            return redirect('/')
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
            return redirect('/')
        else:
            print (form.errors)
    else:
        form = EventForm(instance=event)
    return render(request, 'data/add_event.html', {'form': form})

@login_required
def add_record(request, id=None, event_id=None):
    client = get_object_or_404(Client, pk=request.user.id)
    if client.pro:
        raise PermissionDenied
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
        if form.is_valid():
            record = form.save(commit=False)
            if event_id:
                event = get_object_or_404(Event, pk=event_id)
                record.event = event
                record.save()
                return dashboard(request)  
            else :
                raise PermissionDenied
        else:
            print (form.errors)
        
    else:
        if id:
            form = RecordForm(instance=record)
        else:
            form = RecordForm()
    return render(request, 'data/add_record.html', {'form': form})

@login_required
def add_review(request, id=None, page_id=None):
    client = get_object_or_404(Client, pk=request.user.id)
    if client.pro:
        raise PermissionDenied
    if id:
        review = get_object_or_404(Review, pk=id)
        if review.author != request.user:
            raise PermissionDenied
    else:
        review = None
    if request.method == 'POST':
        if id:
            form = ReviewForm(request.POST, instance=review)
        else:
            form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if page_id:
                page = get_object_or_404(Page, pk=page_id)
                review.page = page
                review.author = request.user
                review.save()
                return redirect('/page/'+str(page_id))
            else :
                raise PermissionDenied
        else:
            print (form.errors)
        
    else:
        if id:
            form = ReviewForm(instance=review)
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
                return redirect('/login')
            else:
                print (extra_form.errors)
        else:
            print (user_form.errors)
            print (client_form.errors)
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard/')
        else:
            user_form = UserForm()
            client_form = ClientForm()
            pro_form = ProUserForm()
            regular_form = RegularUserForm()
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
                return HttpResponseRedirect('/')
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