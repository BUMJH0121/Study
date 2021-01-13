from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.

# Post 상세정보
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Post 목록
def post_list_response(request):
    name = 'Django'
    response = HttpResponse()
    response.write(f'<h2>Hoho {name}</h2>')
    response.write(f'<p>HTTP METHOD:{request.method}</p>')
    response.write(f'<p>HTTP ContentType:{request.content_type}</p>')

    return response
    #return HttpResponse(f'''<h2>Welcome {name}</h2><p>HTTP method:{request.method}</p>''')

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
