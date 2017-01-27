from django.contrib import admin
from pages.models import Page, Preferences

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    fields = ('title', 'subtitle', 'slug', 'body', 'pub_date', 'visible_in_menu', 'show_title', 'image')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Page, PageAdmin)

class PreferencesAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Preferences, PreferencesAdmin)
