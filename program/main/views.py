from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Book, Tag, Comment, Author
from .forms import CommentForm


def index(request):
	obj_list = Book.objects.all()
	paginator = Paginator(obj_list, 1)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'main/pages/index.html', {'page': page, 'posts': posts})


def detail(request, post):
	post = get_object_or_404(Book, slug=post)
	comments = post.comments.filter(active=True)
	new_comment = None 
	comment_form = None 
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.book = post
			new_comment.save()
		else:
			comment_form = CommentForm()
	return render(request, 'main/pages/detail.html', {'post': post, 'comments': comments,
		'new_comment': new_comment, 'comment_form': comment_form})