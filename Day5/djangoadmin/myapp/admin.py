from django.contrib import admin
from myapp.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # pass
    list_display = ["id", "name","age", "rollno"] 
    # list_editable = ["name", "age"] 
    # list_filter = ["age", "name"]
    # search_fields = ["name"]
    # ordering = ["id"]
    # ordering = ["-age", "rollno"]
    ordering = ["id"]
