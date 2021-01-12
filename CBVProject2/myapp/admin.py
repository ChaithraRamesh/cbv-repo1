from django.contrib import admin
from myapp.models import HOD
# Register your models here.
class HODAdmin(admin.ModelAdmin):
	l=['name','no','exp','sal','dept']
admin.site.register(HOD,HODAdmin)
