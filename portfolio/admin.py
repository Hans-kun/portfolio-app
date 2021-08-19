from django.contrib import admin
from .models import Category, Customer, WorkExperience, Post, PostImage

# Register your models here.

class PostImageStackedInline(admin.StackedInline):
    model = PostImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Customer) 
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageStackedInline]
    list_display = ['category', 'title', 'created']
    list_filter = ['title', 'created']