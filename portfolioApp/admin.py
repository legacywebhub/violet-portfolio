from django.contrib import admin
from .models import *
from django.utils.html import format_html

class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ('logo',)
    
    def logo(self, obj):
        return format_html(f'<img src="/media/{obj.logo}" style="width:100px;">')
    
    
class InfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image')

    def image(self, obj):
        return format_html(f'<img src="/media/{obj.my_image}" style="width:100px;">')
    
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'team_image')
    
    def team_image(self, obj):
        return format_html(f'<img src="/media/{obj.image}" style="width:100px;">')
    
    
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'portfolio_image') 
    list_per_page = 10
    
    def portfolio_image(self, obj):
        return format_html(f'<img src="/media/{obj.image}" style="width:100px;">')
    
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email')
    list_filter = ('date',)
    list_per_page = 10
    
class TestimonialAdmin(admin.ModelAdmin):
    list_per_page = 15

# Register your models here.
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Info, InfoAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Testimonial, TestimonialAdmin) 
admin.site.register(Team, TeamAdmin)
admin.site.register(WebsiteSetting, WebsiteSettingAdmin)