from django import forms

from main.models import Product, ContactMessage
from testimonial.models import Testimonial

class ReviewForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 me-4',
            'placeholder': 'Your Name *'
        })
    )
    rate = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        widget=forms.RadioSelect(attrs={'class': 'rating'})
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control border-0',
            'cols': '30',
            'rows': '8',
            'placeholder': 'Your Review *',
            'spellcheck': 'false'
        })
    )
    class Meta:
        model = Testimonial
        fields = ['name', 'rate', 'comment']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']