from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from . models import Image,Profile,NewsLetterRecipients
from .forms import NewsLetterForm,NewImageForm,NewProfileForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome(request):
    images=Image.get_images()
    profile=Profile.get_profile()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('welcome')
            print('valid')
    else:
        form = NewsLetterForm()

    return render(request,'welcome.html',{"images":images,"letterForm":form,"profile":profile})

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term=request.GET.get("category")
        searched_categories=Image.search_by_category(search_term)
        message=f"{search_term}"

        return render(request,"search.html",{"message":message,"categories":searched_categories})
    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def single_photo(request,photo_id):
    try:
        photo=Image.objects.get(id=photo_id)

    except DoesNotExist:
        raise Http404()

    return render(request,'photo.html',{"photo":photo})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('welcome')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})


