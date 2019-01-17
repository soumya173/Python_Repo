from django.db import models

class Book(models.Model):
	book_name = models.CharField(max_length=100)
	book_author = models.CharField(max_length=100)
	book_price = models.CharField(max_length=100)
	book_type = models.CharField(max_length=100)
	book_image_url = models.CharField(max_length=500)
	book_rating = models.CharField(max_length=5)
	book_available = models.CharField(max_length=5)

	def __str__(self):
		return self.book_name + " - " + self.book_author

class Comments(models.Model):
	book_id = models.CharField(max_length=10)
	user_id = models.CharField(max_length=10)
	time_string = models.CharField(max_length=100)
	comment_string = models.CharField(max_length=1000)

	def __str__(self):
		return self.user_id + " commmented on " + self.book_id

class Users(models.Model):
	user_fname = models.CharField(max_length=50)
	user_lname = models.CharField(max_length=50)
	user_email = models.CharField(max_length=50)
	user_profile_url = models.CharField(max_length=500)
	user_phone = models.CharField(max_length=15)

	def __str__(self):
		return self.user_email

class Cart(models.Model):
	user_id = models.CharField(max_length=10)
	book_id = models.CharField(max_length=10)
	order_quantity = models.CharField(max_length=10)

	def __str__(self):
		return self.user_id + " - " + self.book_id



# Commments on books
# Cart
# Users Details