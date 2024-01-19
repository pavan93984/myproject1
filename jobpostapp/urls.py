from django.urls import path
from jobpostapp import views

urlpatterns = [

    path("",views.job,name='job'),
    path("<int:pk>/",views.detail_view.as_view(),name='details'),
    path("create/",views.pavan,name='pavan'),
    

]