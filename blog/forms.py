from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('author',)

    image = forms.ImageField(
        label="Image", required=True, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Type your comment..',
        'rows': '3',
    }), label=False)

    class Meta:
        model = Comment
        fields = ('content', )
