from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from common.models import *
from common.models import User
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ExportMixin

@admin.register(User)
class MyUserAdmin(UserAdmin):
        model = User
        list_display = ('first_name','last_name','phone_number','email')
        list_filter = ('phone_number','email')
        search_fields = ('phone_number', )
        ordering = ('phone_number', )
        filter_horizontal = ()
        fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone_number',)}),)
        # I've added this 'add_fieldset'
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('user_type','email', 'password1', 'password2'),
            }),
    )
        
# Resource for ModelOne
class ModelOneResource(resources.ModelResource):
    class Meta:
        model = Aboutus
        # Specify any specific fields to export, or exclude fields
        fields = ("title",'image_tag',"description")
        
class AboutAdmin(ExportMixin,admin.ModelAdmin):
    resource_class = ModelOneResource
    list_display = ("title",'image_tag',"description")
    
    def image_tag(self, obj):
        if obj.about_images:
            return format_html('<img src="{}" width="50" height="50"/>', obj.about_images.url)
        return "No image found"
    image_tag.short_description = 'Image'
admin.site.register(Aboutus, AboutAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
admin.site.register(Coureses, CourseAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
admin.site.register(Ourteam, TeamAdmin)