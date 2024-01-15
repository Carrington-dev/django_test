from django.contrib import admin

from posts.models import Post

# Register your models here.
class NameAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Post, NameAdmin)
