from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic. base import TemplateView
from django.utils import timezone
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
from django.http import HttpResponse
from django.views import View

# Create your views here.
class MainpageView(TemplateView):
    template_name = 'theme/main.html'

# class BoardView(TemplateView):
#     template_name = 'theme/board.html'

def boardview(request):
    blogs = Blog.objects #모델을 객체로 만든다.
    return render(request, 'theme/board.html',{'blogs':blogs})
    #render 함수는 첫번째 인자로 request, 두번째 인자로 template 이름, 세번째 인자는 선택으로 templates에 전달할 딕셔너리
    #rebder 함수는 주어진 템플릿과 딕셔너리로 랜더링된 결과를 HttpResponse 객체로 리턴한다.

def detaile(request, blog_id, comment=None):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.blog_id=blog
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect('detaile', blog_id)
    else :
        form = CommentForm(instance=comment)
        return render(request, 'theme/detaile.html',{"blog": blog, "form":form})

def comment_edit(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    #get_object_or_404()함수는 데이터베이스에서 객체를 쿼리하여 객체가 존재하지 않을경우 Http404예외를 발생시킨다.
    #get_object_or_404()함수는 첫번째 인자로 Django 모델 객체, 두번째 인자로 임의의 키워드를 추가로 받는다.
    return detaile(request, blog_id, comment)

def write(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.date=timezone.now()
            blog.save()
            return redirect('board')
    else:
        form = BlogForm(instance=blog)
        return render(request,'theme/write.html',{'form':form})


def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    #get_object_or_404()함수는 데이터베이스에서 객체를 쿼리하여 객체가 존재하지 않을경우 Http404예외를 발생시킨다.
    #get_object_or_404()함수는 첫번째 인자로 Django 모델 객체, 두번째 인자로 임의의 키워드를 추가로 받는다.
    return write(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('board')

def comment_remove(request,pk,blog_id):
    comment = get_object_or_404(Comment, pk=pk)
    blog = blog_id
    comment.delete()
    return redirect('detaile', blog_id)
    # return detaile(request, blog_id)

