from django.contrib import admin
from jobpostapp.models import jobpost,apply
from myapp1.models import author,comment

# Register your models here.
admin.site.register(jobpost)
admin.site.register(apply)
admin.site.register(author)
admin.site.register(comment)

