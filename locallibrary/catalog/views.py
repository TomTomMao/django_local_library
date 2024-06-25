from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""
    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    
    # Available books (status = 'a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    print('num_instances_available:', num_instances_available)
    # The 'all()' is implied by default
    num_authors = Author.objects.count()
    
    
    
    context = {
        'num_books': num_books,
        'num_instances': num_instance,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    # paginate_by = 3
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    
class AuthorDetailView(generic.DetailView):
    model = Author