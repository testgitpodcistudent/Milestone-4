from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Post
from django.contrib import messages


def view_blog(request):
    blog_posts = Post.objects.all()

    return render(request, "blog/blog.html", {"blog_posts": blog_posts, })


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
            blog_posts = Post.objects.all()

            return render(request, "blog/blog.html", {"blog_posts": blog_posts, })
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
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_page", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. \
                    Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)