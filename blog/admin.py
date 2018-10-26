from django.contrib import admin
from .models import  BlogArticles
# Register your models here.
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    #数据表中显示的信息(字段)
    list_filter = ("publish","author")
    #用..来过滤
    search_fields=("title","body")
    #搜索,在..字段值内搜索
    raw_id_fields=("author",)
    #未知
    date_hierarchy = "publish"
    #按时间分类(10月26日)
    ordering = ["publish","author"]
admin.site.register(BlogArticles,BlogArticlesAdmin)
