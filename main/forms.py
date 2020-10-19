from django import forms
from django.forms import ModelForm
from main.models import Post, Reporter, Article, Book, Author


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['name']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'pub_date': forms.DateInput(
                attrs = {
                    'type': 'date',
                }
            )
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(
                attrs = {
                    'type': 'date',
                }
            )
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
