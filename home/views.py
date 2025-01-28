from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import blog

def home(req):
    return render(req,'home/home.html')

def contact(req):
    if req.method=='POST':
        name = req.POST['name']
        phone = req.POST['phone']
        email = req.POST['email']
        content = req.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.warning(req,"Please Enter Correct Details")
        else:
            contact = Contact(name=name,phno=phone,email=email,content=content)
            contact.save()
            messages.success(req,"Your Message has Been Delivered")

        # print(name , phone , email ,content)

    return render(req,'home/contact.html')

def about(req):
    return render(req,'home/about.html')

def project(req):
    return render(req,'home/project.html')

def search(req):
    query = req.GET['search']
    print(f"Search query: {query}") 
    
    post = blog.objects.filter(title__icontains=query) if query else [] 
    if post:
        context = {'blog_post': post}
        return render(req, 'home/search.html', context)  
    else:
        return render(req, 'home/notfound.html') 