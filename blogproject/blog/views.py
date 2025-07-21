# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required # To restrict views to logged-in users
from django.contrib import messages # For displaying feedback messages to the user
from .models import Post
from .forms import PostForm # Import the form you just created
from .forms import PostForm, UserRegisterForm # Make sure to import UserRegisterForm
# View to list all blog posts
def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

# View to display a single blog post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

# View to create a new blog post
@login_required # Ensures only logged-in users can create posts
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST) # Get data from the submitted form
        if form.is_valid():
            post = form.save(commit=False) # Create a Post object but don't save to DB yet
            post.author = request.user # Set the author to the currently logged-in user
            post.save() # Now save the post to the database
            messages.success(request, 'Your post has been created!') # Optional: Add a success message
            return redirect('post_detail', pk=post.pk) # Redirect to the newly created post's detail page
    else:
        form = PostForm() # Create an empty form for a GET request (to display it)
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create New Post'})

# View to edit an existing blog post
@login_required # Ensures only logged-in users can edit posts
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Security check: Ensure the logged-in user is the author of the post
    if post.author != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # Populate form with submitted data AND existing instance
        if form.is_valid():
            form.save() # Save the changes to the existing post
            messages.success(request, 'Your post has been updated!') # Optional: Add a success message
            return redirect('post_detail', pk=post.pk) # Redirect to the updated post's detail page
    else:
        form = PostForm(instance=post) # Pre-fill the form with existing post data for a GET request
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Post'})

# Optional: View to delete a blog post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.') # Success message
            return redirect('login') # Redirect to the login page after successful registration
    else:
        form = UserRegisterForm() # Create an empty form for GET requests
    return render(request, 'registration/register.html', {'form': form})