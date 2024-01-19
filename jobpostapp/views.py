from django.shortcuts import render
from jobpostapp.models import jobpost,apply
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.decorators import login_required
from jobpostapp.forms import creatapply
# Create your views here.
@login_required(login_url='user_login')
def job(request):
    pavan=jobpost.objects.all()
    return render(request,"jobpost/jobpost.html",{'pavan':pavan})

class detail_view(DetailView):
    context_object_name = 'details'
    model = jobpost


@login_required(login_url='user_login')
def pavan(request):
    register=False
    form = creatapply
    if request.method == 'POST':
        form = creatapply(request.POST)
        if form.is_valid():
            register=True
            print("application successfully")

    return render(request,"jobpost/create.html",{"form":form,"register":register})










