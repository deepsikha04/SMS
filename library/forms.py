from django import forms
from .models import Book, Transaction, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'quantity']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'role']
