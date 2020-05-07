from django.contrib import admin
from page.models import Post,PageComment

# Register your models here.
admin.site.register((PageComment))
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)