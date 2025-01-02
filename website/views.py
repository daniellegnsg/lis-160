from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddBookForm
from .models import Book


def home(request):
	books = Book.objects.all()

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in!")
			return redirect('home')
		else:
			messages.success(request, "There was an error logging in. Please try again.")
			return redirect('home')
	else:
		return render(request, 'home.html', {'books':books})



def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out.")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have successfully registered. Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def about_book(request, pk):
	if request.user.is_authenticated:

		about_book = Book.objects.get(id=pk)
		return render(request, 'book.html', {'about_book':about_book})
	else:
		messages.success(request, "You must be logged in to view that page.")
		return redirect('home')



def delete_book(request, pk):
	if request.user.is_authenticated:
		delete_it = Book.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Book deleted successfully.")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in to do that action.")
		return redirect('home')



def add_book(request):
	form = AddBookForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_book = form.save()
				messages.success(request, "Book added successfully.")
				return redirect('home')
		return render(request, 'add_book.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to do that action.")
		return redirect('home')


def update_book(request, pk):
	if request.user.is_authenticated:
		current_book = Book.objects.get(id=pk)
		form = AddBookForm(request.POST or None, instance=current_book)
		if form.is_valid():
			form.save()
			messages.success(request, "Book updated successfully.")
			return redirect('home')
		return render(request, 'update_book.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to do that action.")
		return redirect('home')

