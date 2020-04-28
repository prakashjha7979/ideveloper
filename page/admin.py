from django.contrib import admin
from page.models import Post,PageComment
# Register your models here.
admin.site.register((Post,PageComment))
