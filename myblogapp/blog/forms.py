from django import forms

from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
