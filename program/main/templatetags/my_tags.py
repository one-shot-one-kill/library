from django import template
from django.db.models import Count

from ..models import Book

register = template.Library()


@register.simple_tag
def most_commented_post(count=5):
	return Book.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]