from django.shortcuts import render, get_object_or_404

from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books":books})

def book_detail(request, id):
    # book = Book.objects.get(pk=id)

    book = get_object_or_404(Book, pk=id)

    return render(request, "book_detail.html", {
        "title" : book.title,
        "author": book.author,
        "ratings": book.ratings,
        "is_bestselling": book.is_bestselling
    })