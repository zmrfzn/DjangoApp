from django.shortcuts import render
from .models import post
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts = post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'blog/post_list.html', {'posts':posts})