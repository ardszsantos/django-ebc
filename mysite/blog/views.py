from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        status = 1

        if title and content:
            slug = slugify(title)
            post = Post.objects.create(
                title=title,
                slug=slug,
                author=request.user,
                content=content,
                status=status,
            )
            return redirect('post_detail', slug=post.slug)

    return render(request, 'blog/post_create.html')
