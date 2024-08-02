from django.contrib import admin


class PostAdmin(admin.ModelAdmin):

    ordering = ['created_at']
    list_display = ['user_id', 'title', 'display_categories', 'created_at']
    list_filter = ['country', 'city', 'created_at']

    def display_categories(self, obj):
        return ', '.join(category.name for category in obj.category.all())
    display_categories.short_description = 'Categories'


class PhotoAdmin(admin.ModelAdmin):

    list_display = ['post']


from travel import models
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Category)
