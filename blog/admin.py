# coding:utf-8
from django.contrib import admin
from models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'desc', 'click_count',)
	list_display_links = ('title', 'desc',)
	list_editable = ('click_count',)

	fieldsets = (
		(None, {
			'fields': ('title', 'desc', 'content',)
		}),
		('高级设置', {
		'classes': ('collapse',),
		'fields': ('enable_comments', 'registration_required', 'template_name')
	}),
		)

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
