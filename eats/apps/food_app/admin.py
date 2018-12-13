from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)

# class UserStripeAdmin(admin.ModelAdmin):
#     class Meta;
#         model = UserStripe

# admin.site.register(UserStripe, UserStripeAdmin)