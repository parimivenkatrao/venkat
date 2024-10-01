from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin
class PostAdmin(ImportExportModelAdmin):
    list_display = ('fullname', 'dateofbarth', 'gender', 'phone', 'email', 'create_at', 'is_published','username','password')
    list_filter = ('gender', 'create_at', 'is_published')
    list_display_links = ('fullname','phone')

    """def dateofbarth_formatted(self, obj):
        return obj.dateofbarth.strftime('%Y-%m-%d') if obj.dateofbarth else '-'
    dateofbarth_formatted.short_description = 'Date of Birth'

    def create_at_formatted(self, obj):
        return obj.create_at.strftime('%Y-%m-%d') if obj.create_at else '-'
    create_at_formatted.short_description = 'Created At'"""

admin.site.register(Post, PostAdmin)

