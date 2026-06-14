from django.contrib import admin
from .models import *

admin.site.register(Warden)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Fee)
admin.site.register(Complaint)