from django.shortcuts import render,get_object_or_404
#get_object_or_404引入异常处理
#可以用try:...except:...捕获
#在except 中使用raise Http404()来处理
from .models import BlogArticles
# Create your views here.
def blog_title(request):
    blogs=BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})
def blog_article(request,article_id):
    #article=BlogArticles.objects.get(id=article_id)
    article=get_object_or_404(BlogArticles,id=article_id)
    pub=article.publish
    return render(request,"blog/content.html",{"article":article,"publish":pub})