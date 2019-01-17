from django.views import generic
from .models import Book, Comments

class IndexView(generic.ListView):
	template_name = 'books/index.html'

	def get_queryset(self):
		return Book.objects.all()

class DetailView(generic.DetailView):
	model = Book
	template_name = 'books/details.html'



# from django.shortcuts import render
# from django.http import HttpResponse, Http404
# from .models import Book, Comments, Users
# from django.template import loader
# from django import template

# def index(request):
# 	all_books = Book.objects.all()
# 	# template = loader.get_template('books/index.html')

# 	context = {
# 		'all_books': all_books
# 	}

# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'books/index.html', context)

# def details(request, book_id):
# 	try:
# 		book = Book.objects.get(id=book_id)
# 	except Book.DoesNotExist:
# 		raise Http404("Book Does Not Exists")

# 	try:
# 		comments = Comments.objects.get(book_id=book_id)
# 	except Comments.DoesNotExist:
# 		pass

# 	try:
# 		commented_user = Users.objects.get(id=comments.user_id)
# 	except Users.DoesNotExist:
# 		commented_user = ""

# 	active_star = ""
# 	inactive_star = ""
# 	for x in range(int(book.book_rating)):
# 		active_star += "-"

# 	for x in range(5 - int(book.book_rating)):
# 		inactive_star += "-"

# 	context = {
# 		'book': book,
# 		'comments': comments,
# 		'user': commented_user,
# 		'rating': active_star,
# 		'remaining': inactive_star
# 	}

# 	return render(request, 'books/details.html', context)