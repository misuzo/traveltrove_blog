from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user_id', 'get_username', 'country']
    list_filter = ['country']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'


admin.site.register(Profile, ProfileAdmin)
