from django.shortcuts import render,redirect,get_object_or_404
from .forms import userform,imgpro1,daily_post,commentform,subscribes
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from jobpostapp.models import apply
from myapp1.models import author,comment
# Create your views here.
def register(request):
    submit = False
    if request.method == 'POST':
        leo = imgpro1(request.FILES)
        form = userform(request.POST)

        if form.is_valid() and leo.is_valid():
            user = form.save()
            user.save()
            prof = leo.save(commit=False)
            prof.user = user
            submit =True
            print("username :",form.cleaned_data.get("username"))

        else:
            return HttpResponse("Data was not saved please try again")
            
    else:
        leo =imgpro1()
        form =userform()
    return render(request,"register.html",{"form":form,"submit":submit,'leo':leo})
@login_required(login_url='user_login')
def index(request):
    return render(request,"index.html")

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password =request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('homepro')
            else:
                return HttpResponse(" please check your creds")
        
        else:
            return HttpResponse("please check your creds")
        
    return render(request,"login.html",{})


@login_required(login_url='user_login')    
def homepro(request):
    raj = author.objects.all().order_by("-view_count")[0:3]
    raju = author.objects.all().order_by("-view_count")[0:1]
    raja = author.objects.all().order_by("-time")[0:3]
    remo = subscribes()
    saved = False
    if request.method == "POST":
        remo = subscribes(request.POST)
        if remo.is_valid():
            remo.save()
            saved = True
            print("subscribes successfully")

    return render(request,"homepro.html",{"raj":raj,"remo":remo,"saved":saved,"raja":raja,'raju':raju})


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')


def profile(request):
    return render(request,"profile/user_profile.html",{})




def daily_posts(request):
    day = daily_post()
    if request.method == 'POST':
        day = daily_post(request.POST,request.FILES)
        if day.is_valid():
            # day.save(commit=False)
            day.save()
            print("posted successfull")

    return render(request,'profile/add_post.html',{"day":day})



def blog(request):
    rana=author.objects.all()
    return render(request,'blog.html',{"rana":rana})

def jdetails(request, pk):
    j = author.objects.get(pk=pk)
    cform = commentform()
    raj = author.objects.all()
    raju = author.objects.all().order_by("-view_count")[0:3]
    raja = author.objects.all().order_by("-time")[0:2]


    #like code

    liked = False
    if j.like.filter(id=request.user.id).exists():
        liked = True
    post_is_liked = liked
    number_of_likes = j.number_of_likes()    
    print("hi")

    # bookmark code
    booked = False
    if j.bookmarks.filter(id=request.user.id).exists():
        booked = True
    post_is_booked = booked
    print("hello") 


    if request.method == 'POST':
        print("data coming")
        cform = commentform(request.POST) 
        if cform.is_valid():
            parent_obj = None
            if request.POST.get('parent'):
                # save reply
                parent=request.POST.get('parent')
                parent_obj = comment.objects.get(id=parent)
                if parent_obj:
                    comment_reply = cform.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = j
                    comment_reply.save()
            else:
                print("valid success")
                print(request.POST.get('Name'))
                print(request.POST.get('Email'))
                comment1 = cform.save(commit=False)
                print(comment1)
                postid = request.POST.get('post_id')
                # print("id->",postid)
                post = author.objects.get(id=postid)
                # print('hii')
                comment1.post = post
                # print('hello')
                comment1.save()

    if j.view_count is None:
        j.view_count = 1
    else:
        j.view_count = j.view_count + 1
    j.save()
    k = comment.objects.filter(post=j)
    context = {'j':j, 'cform':cform,'k':k,'raj':raj,'post_is_liked':post_is_liked,'number_of_likes':number_of_likes,"post_is_booked":post_is_booked,"raju":raju,'raja':raja}
    return render(request, 'blog_detail.html',context)

def search(request):
    raj = author.objects.all().order_by("-view_count")[0:3]
    raja = author.objects.all().order_by("-time")[0:3]
    saved = False
    if request.method == 'POST':
        search_qry = request.POST.get('search_query')
        posts = author.objects.filter(post_type__contains=search_qry)
        print(search_qry)
        saved = True
        return render(request,'search.html',{'search_query':search_qry,'posts':posts,"raj":raj,'raja':raja,'saved':saved})
    else:
        return render(request,'search.html',{"raj":raj,'raja':raja,'saved':saved}) 
    
def like_post(request,pk):
    print(request.POST.get('post_id'))
    posts =get_object_or_404 (author,id=request.POST.get('post_id'))
    if posts.like.filter(id=request.user.id).exists():
        posts.like.remove(request.user)
    else:
        posts.like.add(request.user)
    return redirect('bdetail',pk=pk)

def booked(request,pk):
    print(request.POST.get('post_id'))
    posts =get_object_or_404 (author,id=request.POST.get('post_id'))
    if posts.bookmarks.filter(id=request.user.id).exists():
        posts.bookmarks.remove(request.user)
    else:
        posts.bookmarks.add(request.user)
    return redirect('bdetail',pk=pk)
    
def likes(request):
    qa = author.objects.filter(like = request.user)
    print(qa)
    return render(request,'likes.html',{"qa":qa})

def bookmark(request):
    q = author.objects.filter(bookmarks = request.user)
    print(q)
    return render(request,'bookmarks.html',{"q":q})
    

def job_posts(request):
    
    rana = apply.objects.all()
    print(rana)
    return render(request,"profile/job_post.html",{'rana':rana})