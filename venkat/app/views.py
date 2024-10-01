from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib.auth import authenticate, login,logout
from datetime import datetime
from django.http import HttpRequest,HttpResponse
import csv  # Add this import
#from django.http import HttpResponse

# Create your views here.



def pvrcblog(request):
    post = Post.objects.all().filter(is_published = True).order_by('-create_at')

    context = {
        'posts' : post
    }

    return render(request,'pvrcblog.html',context)

def home(request):

    '''name = 'parimi venkataro'
    age = '20'''
    time = datetime.now()
    return render(request,"home.html",{'time': time})




def contact(request,id):
    post = Post.objects.get(id = id)

    post.delete()

    return redirect('pvrcblog')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        fullname = request.POST.get('fullname', '')
        dateofbarth = request.POST.get('dateofbarth', '')
        gender = request.POST.get('gender','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        img = request.FILES.get('img', None)  # Use request.FILES for file uploads
        video_file = request.FILES.get('video', None)  # Assuming 'video' is a file upload field
        

        # Create a new Video instance and save it
        video = Post(username = username,fullname=fullname,  dateofbarth= dateofbarth,gender=gender,phone=phone,email=email, img=img, video=video_file)
        video.save()
        return redirect('pvrcblog')
        #return render(request, 'register.html')  # Adjust the path as per your template structure
  # Adjust the path as per your template structure



    return render(request,'register.html')

def update(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        dateofbarth = request.POST.get('dateofbarth', '')
        gender = request.POST.get('gender','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        img = request.FILES.get('img', None)  # Use request.FILES for file uploads
        video_file = request.FILES.get('video', None)

        post.fullname = fullname
        post.dateofbarth = dateofbarth
        post.gender = gender
        post.phone = phone
        post.email = email
        post.img = img
        post.video  = video_file 
        post.save()

        return render(request, 'update.html',{'post': post})

    else:
        context = {'post': post}
        return render(request, 'update.html', context)
    
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pvrcblog')
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def sinout(request):
    logout(request)
    return redirect('home')

def down(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="users_csv"'

    writer = csv.writer(response)
    writer.writerow(['Full Name', 'Date of Birth', 'Gender', 'Phone', 'Email', 'Created At', 'Is Published'])

    posts = Post.objects.all().values_list('fullname', 'dateofbarth', 'gender', 'phone', 'email', 'create_at', 'is_published')
    for user in posts:
        writer.writerow(user)
    return response
"""def page_404(request,Exceptions):
    return render(request,'page_404.html')"""