from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'pub_date')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
