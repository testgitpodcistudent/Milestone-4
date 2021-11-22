from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, CommentForm
from .models import Post, Comment
from django.contrib import messages


def view_blog(request):
    blog_posts = Post.objects.all()

    return render(request, "blog/blog.html", {"blog_posts": blog_posts, })


@login_required()
def post_page(request, post_id):
    """display individual product detail page"""
    form = CommentForm(request.POST)
    if form.is_valid():
        post = get_object_or_404(Post, pk=post_id)
        form.instance.user = request.user
        form.instance.post = post
        form.save()
        return redirect(reverse("post_page", args=[post.id]))

    post = get_object_or_404(Post, pk=post_id)
    post_comments_count = Comment.objects.all().filter(post=post.id).count()
    post_comments = Comment.objects.all().filter(post=post.id)
    context = {
        'post': post,
        'form': form,
        'post_comments': post_comments,
        'post_comments_count': post_comments_count,
    }

    return render(request, "blog/post_page.html", context)


@login_required
def create_post(request):
    """Add a post to the blog"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            messages.success(request, "Post added successfully!")
            return redirect(reverse("post_page", args=[blog_post.id]))
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


@login_required
def edit_post(request, post_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse("home"))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited post!")
            return redirect(reverse("view_blog"))
        else:
            messages.error(
                request, "Failed to edit post. \
                    Please ensure the form is valid."
            )
    else:
        form = BlogForm(instance=post)
        messages.info(request, f"You are editing {post.title}")

    template = "blog/edit_post.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only admins can do that.")
        return redirect(reverse("home"))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, "Post deleted!")

    return redirect(reverse("view_blog"))
