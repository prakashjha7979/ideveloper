from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from page.models import Post
# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('this is home')


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request,'home/contact.html')

    # return HttpResponse('this is contact')

def about(request):
    return render(request,'home/about.html')

    # return HttpResponse('this is about')
def search(request):
    query = request.GET['query']
    if len(query)>75:
        allPosts = Post.objects.none()
        # allPosts = Post.objects.all()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query")
    params = {'allPosts':allPosts, 'query':query} 
    return render(request, 'home/search.html', params)
    
def handlesignup(request):
    if request.method == 'POST':
        #get the post parametres
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        emailaddress = request.POST['emailaddress']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        #username should be under 10 charecters
        if len(username) > 10:
            messages.error(request, "username must under 10 words")
            return redirect('home')

        #username must contain alpha-numeric charecters    
        if not username.isalnum():
            messages.error(request, "username must contain only letters and numbers")
            return redirect('home')
        #passwords should matched
        if pass1 != pass2:
            messages.error(request, "Passwords did not matched! write again")
            return redirect('home')

        #create User
        myuser= User.objects.create_user(username, emailaddress , pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your ideveloper account has been successfully created")
        return redirect('home')









    else:
        return HttpResponse('404 -Not Found')
    #return HttpResponse('this is search')

def handlelogin(request):
    if request.method == 'POST':
        #get the post parametres
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials, please try again")
            return redirect('home')
    return HttpResponse('404- Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')                
    
