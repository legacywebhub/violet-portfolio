from django.urls import path
from .sitemaps import StaticViewSitemap, ContentSitemap
from django.contrib.sitemaps.views import sitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
    'content': ContentSitemap,
}

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contents/', views.contents, name="contents"),
    path('content/<str:pk>/', views.content, name="content"),
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
]
