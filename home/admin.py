# from django.contrib import admin
# from django import forms
# from home.models import Blog
#
# # Register your models here.
# class BlogAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
#
#     class Meta:
#         model = Blog
#         fields = "__all__"
#
# class BlogAdmin(admin.ModelAdmin):
#     form = BlogAdminForm
#
# admin.site.register(Blog, BlogAdmin)
from django.contrib import admin
from django import forms
from home.models import Project

# Register your models here.
class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))  # Updated for Project's description field

    class Meta:
        model = Project
        fields = "__all__"

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

admin.site.register(Project, ProjectAdmin)
