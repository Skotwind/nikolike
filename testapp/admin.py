from django.contrib import admin
from .models import Photo, CommentPhoto


class PhotoInline(admin.StackedInline):  # указывает связь
    model = CommentPhoto
    extra = 2  # колличество коментариев под статьей


class PhotoAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_filter = ['Photo_date']


admin.site.register(Photo, PhotoAdmin)
# Register your models here.





