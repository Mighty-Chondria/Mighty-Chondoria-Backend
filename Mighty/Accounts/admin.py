from django.contrib import admin
from .models import UserAdmin
# Register your models here.


admin.site.site_header='MightyChondria'


admin.site.register(UserAdmin)
