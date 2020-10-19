from django.shortcuts import render, redirect
from main.forms import PostForm, ReporterForm, ArticleForm, BookForm, AuthorForm
from main.models import Post, Reporter, Article, Book, Author


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': posts})


def list_reporters(request):
    reporters = Reporter.objects.all()
    return render(request, 'list_reporters.html', {'reporters': reporters})


def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'list_articles.html', {'articles': articles})


def list_authors(request):
    authors = Author.objects.all()
    return render(request, "list_authors.html", {'authors': authors})


def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {'books': books})



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_posts')
    else:
        form = PostForm()
        return render(request, 'add.html', {'form': form})


def add_reporter(request):
    if request.method == "POST":
        form = ReporterForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_reporters')
    else:
        form = ReporterForm()
        return render(request, 'add.html', {'form': form})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
        return render(request, 'add.html', {'form': form})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_authors')
    else:
        form = AuthorForm()
        return render(request, "add.html", {'form': form})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_books')
    else:
        form = BookForm()
        return render(request, 'add.html', {'form': form})