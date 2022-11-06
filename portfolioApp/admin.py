from django.contrib import admin
from .models import *
from django.utils.html import format_html

class InfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image')

    def image(self, obj):
        return format_html(f'<img src="https://res.cloudinary.com/legacy-web-tech/image/upload/v1/{obj.my_image}" style="width:100px;">')
    
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'team_image')
    
    def team_image(self, obj):
        return format_html(f'<img src="https://res.cloudinary.com/legacy-web-tech/image/upload/v1/{obj.image}" style="width:100px;">')
    
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'portfolio_image') 
    list_per_page = 10
    
    def portfolio_image(self, obj):
        return format_html(f'<img src="https://res.cloudinary.com/legacy-web-tech/image/upload/v1/{obj.image}" style="width:100px;">')
    
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'less_subject', 'email')
    list_filter = ('date',)
    list_per_page = 10
    
    def less_subject(self, obj):
        return obj.subject[:50]
    
class ContentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'less_title',)
    list_filter = ('created_at', 'last_modified')
    list_per_page = 10
    
    def less_title(self, obj):
        return obj.title[:50]
    
class TestimonialAdmin(admin.ModelAdmin):
    list_per_page = 15

# Register your models here.
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(PortfolioCategory)
admin.site.register(Info, InfoAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Testimonial, TestimonialAdmin) 
admin.site.register(Team, TeamAdmin)
admin.site.register(WebsiteSetting)