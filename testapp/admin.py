from django.contrib import admin
from testapp.models import Student,Submarks,Friendlist,Hotel,Emp,Contactor
from django.contrib.admin import AdminSite,ModelAdmin


class StoreAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'password', 'marks']

@admin.register(Emp)
class Empadmin(admin.ModelAdmin):
    list_display = ['id','name','marks']

# Register your models here.
admin.site.register(Student,StoreAdmin)
admin.site.register(Submarks)
admin.site.register(Friendlist)
admin.site.register(Hotel)




@admin.register(Contactor)
class ContractModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'age','salary']








