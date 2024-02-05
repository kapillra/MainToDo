from django.contrib import admin
from .models import *

admin.site.register(Role)
admin.site.register(Master)
admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(ToDoList)
admin.site.register(TaskAssociation)