from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserCreation, AddPostForm
from .models import Post


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'main.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'postdetail.html', {'post': post})


class AddPost(View):
    def get(self, request):
        context = {
            'form': AddPostForm
        }
        return render(request, 'addpost.html', context)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, 'addpost.html', context)


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreation
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = UserCreation(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)