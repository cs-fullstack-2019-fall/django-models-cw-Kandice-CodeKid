from django.contrib import admin

# Register your models here.
from .models import Dog
from .models import AccountUser

admin.site.register(Dog)
admin.site.register(AccountUser)