from django.contrib import admin

from builder.models import   Users,Contact,Product

admin.site.site_header="ResumeX"
admin.site.index_title = "Welcome to ResumeX the Resume Builder Admin Panel!"
# Users
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'contact',  'password')

admin.site.register(Users, UserAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'content')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'title', 'description', 'price','tags')