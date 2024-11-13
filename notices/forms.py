from django import forms
from .models import Notice, Category, Tag


class NoticeForm(forms.ModelForm):
    expiry_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Expiry Date (optional)"
    )
     # Multiple choice fields for categories and tags
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    

    class Meta:
        model = Notice
        fields = ['title', 'content', 'image', 'expiry_date', 'categories', 'tags', 'file']  # Include 'image' in the fields

