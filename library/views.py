from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Transaction, Member
from .forms import BookForm, CheckoutForm, MemberForm

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

@login_required
def book_checkout(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    member = get_object_or_404(Member, user=request.user)

    if book.quantity > 0:
        Transaction.objects.create(book=book, member=member)
        book.quantity -= 1
        book.save()
        return redirect('book_list')
    return render(request, 'library/book_list.html', {'error': 'Not enough copies available.'})

@login_required
def book_return(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if not transaction.returned:
        transaction.returned = True
        transaction.book.quantity += 1
        transaction.book.save()
        transaction.save()
    return redirect('book_list')

@login_required
def member_register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = MemberForm()
    return render(request, 'library/member_form.html', {'form': form})
