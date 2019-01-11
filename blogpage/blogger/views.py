from django.shortcuts import redirect , render
from django.shortcuts import HttpResponse
from . import models
from  blogger.models import blog_article



# Create your views here.
def home(request):
    article=models.blog_article.objects.all()
    context={'article':article}
    return render (request,'home.html',context)
def blog_detail(request,blog_id):
    obj=models.blog_article.objects.filter(id=blog_id)
    context={
        'obj':obj
    }
    return render(request,'blog_detail.html',context)


def register(request):
    if request.method=='POST':
        name = request.POST['name']
        pwd=request.POST['password']
        email=request.POST['email']
        if models.register.objects.filter(name=name).exists():
            alert={'username':'username already exists'}
            return render(request, 'users/registration.html',alert)

        else:
            reg_ob=models.register()
            reg_ob.name=name
            reg_ob.password=pwd
            reg_ob.email=email
            reg_ob.save()
            print('name:', name, 'password:', pwd)  # this will print on terminal
            context={
            'msg':'congratulations your data has been saved now securely login to your acount'
            }
            return render(request ,'users/login.html',context)
    return render(request,'users/registration.html')

def login(request):
    if request.session.has_key('username'):
        return render(request,'user-blog/create-blog.html')

    if request.method =='POST':
        name=request.POST['name']
        pwd=request.POST['password']
        print ("user:" ,name,"pass :", pwd ,)
        log_ob=models.register.objects.filter(name=name,password=pwd)
        if (len(log_ob)< 1) :
            context = {
                'msg':"wrong password...."
            }
            return render(request, 'users/login.html', context)
        else:
            request.session['username']=name



            return render(request,'user-blog/create-blog.html')


    return render(request,'users/login.html')

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request,'users/login.html')




def create_blog(request):
    if request.method=='POST':
        author=request.POST['author']
        title=request.POST['title']
        category=request.POST['cat']
        content=request.POST['content']
        img=request.POST['img']
        obj_blog=models.blog_article()
        obj_blog.author=author
        obj_blog.title=title
        obj_blog.category=category
        obj_blog.content=content
        obj_blog.image=img
        obj_blog.save()
        print('hello')
        article = models.blog_article.objects.all()
        context={
            'msg':'blog created successfully ..',
             'user':obj_blog.author,
            'article': article
        }
        return render(request,'home.html',context)


























