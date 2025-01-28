from django.shortcuts import render,HttpResponse
from . models import blog
from django.contrib import messages
from home.models import Contact
# Create your views here.

def bloghome(req):
    blogs=blog.objects.all();
    context = {'blog_post':blogs}
    return render(req,'blog/bloghome.html',context)


def blogpost(req,slug):
    blog_post=blog.objects.filter(slug=slug).first()
    context = {'post':blog_post}
    return render(req ,'blog/blogpost.html',context)

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

