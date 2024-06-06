from django.contrib import admin

# Register your models here
from .models import CustomUser,Package,Comments,Blogs,Review
# admin.site.register(CustomUser)
class CustomUseryadmin(admin.ModelAdmin):
    list_display = ['username','is_superuser']
admin.site.register(CustomUser,CustomUseryadmin)

class Packageadmin(admin.ModelAdmin):
    list_display = ['admin','title','amount','location','duration']
admin.site.register(Package,Packageadmin)

class Commentsadmin(admin.ModelAdmin):
    list_display = ['user','comment','package']
admin.site.register(Comments,Commentsadmin)

class Blogsadmin(admin.ModelAdmin):
    list_display = ['user','title']
admin.site.register(Blogs,Blogsadmin)

class Reviewadmin(admin.ModelAdmin):
    list_display = ['user','review']
admin.site.register(Review,Reviewadmin)