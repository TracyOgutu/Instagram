from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from . models import Image,Profile,NewsLetterRecipients,Comments
from .forms import NewsLetterForm,NewImageForm,NewProfileForm,NewCommentForm,UpdateProfileForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    '''
    View for the main homepage.It retrieves authenticated user posts and posts for other users stories
    '''
    everyoneimages=Image.get_images()
    comment=Comments.get_comments()
    users = User.objects.all()
    logged_in_user = request.user
    
    logged_in_user_posts = Image.objects.filter(editor=logged_in_user)
    try:
        profile=Profile.objects.get(editor=logged_in_user)
    except Profile.DoesNotExist:
        profile=None
    
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

    return render(request,'index.html',{"everyone":everyoneimages,"images":logged_in_user_posts,"letterForm":form,"profile":profile,"comment":comment,"users":users})

def search_category(request):
    '''
    This method searches for an image by using the name of the image
    '''
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
    '''
    This method displays a single photo and its details such as comments, date posted and caption
    '''

    if request.method=='POST':

        form=NewCommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.editor=request.user      
            post=Image.objects.get(id=photo_id)
            comment.image_foreign=post
            comment.save()
            HttpResponseRedirect('single_photo')
    else:
        form=NewCommentForm()

    image_posted=Image.single_image(photo_id)  
    imageId=Image.get_image_id(photo_id)
    comments=Comments.get_singlepost_comments(imageId)
        
    # try:
    #     photo=Image.objects.get(id=photo_id)

    # except DoesNotExist:
    #     raise Http404()

    return render(request,'photo.html',{"form":form,"comments":comments,"photo":image_posted})

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
    '''
    Used for creating a new profile for the user. It includes a profile photo and a bio
    '''
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

def makecomment(request):
    '''
    View for making a comment 
    '''
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor = current_user
            comment.save()
        return redirect('welcome')

    else:
        form = NewCommentForm()
    return render(request, 'comment.html', {"form": form})
   
def delete_post(request,post_id=None):
    '''
    View for deleting a post by the user
    '''
    post_to_delete=get_object_or_404(Image,id=post_id)
    post_to_delete.delete()
    return redirect('welcome')

def like_a_post(request):
    '''
    View for liking a post
    '''
    post = get_object_or_404(Image,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('welcome')

def follow(request):
    '''
    View for following a user
    '''
    post = get_object_or_404(Image,id=request.POST.get('post_id'))
    post.followers.add(request.user)
    return redirect('welcome')

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    '''
    View for editing the profile 
    '''
    if request.method=='POST':
        profileform=UpdateProfileForm(request.POST,request.FILES,instance=request.user)
        if profileform.is_valid():
            profileform.save()
            
        return redirect('welcome')
    else:
        profileform=UpdateProfileForm(instance=request.user)
    
    context={
        'profileform':profileform,
    }
    return render(request,'updateprofile.html',context)


@login_required(login_url='/accounts/login/')
def display_profile(request,user_id):
    '''
    View for displaying the profile for a single user
    '''
    try:
        single_profile=Profile.single_profile(user_id)              
        image_posted=Image.user_images(user_id)
        return render(request,'profiledisplay.html',{"profile":single_profile,"image":image_posted})
    except Profile.DoesNotExist:
        messages.info(request,'The user has not set a profile yet')
        return redirect('welcome')


    