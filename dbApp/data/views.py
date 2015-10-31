from django.shortcuts import render
from .forms import UserForm, ClientForm, PageForm, RecordForm, ReviewForm, DiseaseForm, EventForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print form.errors
    else:
        form = PageForm()
    return render(request, 'data/add_page.html', {'form': form})

def add_disease(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print form.errors
    else:
        form = DiseaseForm()
    return render(request, 'data/add_disease.html', {'form': form})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print form.errors
    else:
        form = EventForm()
    return render(request, 'data/add_event.html', {'form': form})

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print form.errors
    else:
        form = RecordForm()
    return render(request, 'data/add_record.html', {'form': form})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return register(request)
        else:
            print form.errors
    else:
        form = ReviewForm()
    return render(request, 'data/add_review.html', {'form': form})

def index(request):
	return render(request, 'data/index.html', {})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = ClientForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ClientForm()

    # Render the template depending on the context.
    return render(request,
            'data/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



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
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'data/login.html', {})


def ajax_login(request):

    if request.method == 'POST':
        data = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if (not user is None) and (user.is_active):
            login(request, user)
            if not request.POST.get('rem', None):
                request.session.set_expiry(0)
            data['success'] = "You have been successfully Logged In"
        else:
            data['error'] = "There was an error logging you in. Please Try again"
        return JsonResponse(data)
    else:
    	return render(request, 'data/login.html', {})