from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.views.generic import ListView, DetailView
from .models import Post


def view_blog(request):
    blog_posts = Post.objects.all()


    return render(request, "blog/blog.html", {"blog_posts":blog_posts,})


@login_required
def create_post(request):
    """Add a post to the blog"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, "Post added successfully!")
            return redirect(reverse("view_blog", args=[blogpost.id]))
        else:
            messages.error(
                request, "Failed to add post. \
                    Please ensure the form is valid."
            )
    else:
        form = BlogForm()

    template = "blog/create_post.html"
    context = {
        "form": form,
    }

    return render(request, template, context)