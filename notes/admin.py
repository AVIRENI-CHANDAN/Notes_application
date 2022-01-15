from django.contrib import admin

# Register your models here.
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('fullname','username','password','email','created_at','isActive')
    readonly_fields = ('email','username','password','created_at')


admin.site.register(UserModel,UserModelAdmin)