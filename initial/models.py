from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    edition = models.DateField(null=True)
    bookcover = models.ImageField(upload_to='bookcover_folder', null=True, blank=True)
    #descripcion = ..RichField
    createdbyuser = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"Title: {self.title} - Author: {self.author} - Isbn: {self.isbn} - Edition: {self.edition} - bookcover: {self.bookcover} - createdbyuser: {self.createdbyuser}"
    
class Client(models.Model):
    dni = models.IntegerField()
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20, null=True)
    #observaciones = ..RichField
    createdbyuser = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"LastName: {self.lastname} - FirstName: {self.firstname} - Dni: {self.dni} - createdbyuser: {self.createdbyuser}"
    
class User(models.Model):
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    userpass = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Fullname: {self.fullname} - UserName: {self.username} - UserPassword: {self.userpass}"
    