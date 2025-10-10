from django.contrib import admin
from .models import Donor, Student, Request, Admin

admin.site.register(Donor)
admin.site.register(Student)
admin.site.register(Request)
admin.site.register(Admin)