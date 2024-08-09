from django.contrib import admin

from travel.models import Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class PostAdmin(admin.ModelAdmin):

    ordering = ['created_at']
    list_display = ['author_username', 'title', 'display_categories', 'created_at']
    list_filter = ['country', 'city', 'created_at']
    inlines = [PhotoInline]

    def author_username(self, obj):
        return obj.author.username if obj.author else 'No Author'
    author_username.short_description = 'Author'

    def display_categories(self, obj):
        return obj.category.get_cat_name_display() if obj.category else '-'
    display_categories.short_description = 'Category'


class PhotoAdmin(admin.ModelAdmin):

    list_display = ['post']

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['cat_name']


from travel import models
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Photo, PhotoAdmin)
admin.site.register(models.Category, CategoryAdmin)
