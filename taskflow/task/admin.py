from django.contrib import admin
from .models import Task


# Register your models here.
admin.site.register(Task)
class TaskAdmin(Task):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title','description')