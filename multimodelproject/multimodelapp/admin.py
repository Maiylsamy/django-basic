from django.contrib import admin

from multimodelapp.models import Book,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "name","publish_date"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name","email"]

# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)