from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Content

class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'contents',
            'portfolio',
        ]

    def location(self, item):
        return reverse(item)

class ContentSitemap(Sitemap):
    def items(self):
        return Content.objects.all()