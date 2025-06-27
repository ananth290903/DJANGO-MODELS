from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse 

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.TextField(null=True,max_length=100)
    is_bestselling=models.BooleanField(default=False)

    def __str__(self):
        return f"({self.title}) ({self.rating})"
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[self.id])
    
























'''
Data Enities
They are blueprnt for data objects

>>> Book.objects.all()
<QuerySet [<Book: (Lord of the Rings) (3)>, <Book: (Driving School) (5)>, <Book: (Kalluvaathukkal Kathreena) (3)>, <Book: (Kinnara Thumbikkal) (5)>]>
>>> Book.objects.create(title="Layanam",rating=4,author="Thulasidas",is_bestselling=True)
<Book: (Layanam) (4)>
>>> Book.objects.get(author="Thulasidas")
<Book: (Layanam) (4)>


> harry_potter=Book.objects.all()[0]
>harry_potter
<Book: (The Philosopher 's Stone) (3)>
> harry_potter.author="JK Rowling"
> harry_potter.is_bestselling=True
> harry_potter.save()
> Book.objects.all()
<QuerySet [<Book: (The Philosopher 's Stone) (3)>, <Book: (Lord of the Rings) (3)>]>
> Book.objects.all()[0]
<Book: (The Philosopher 's Stone) (3)>
> Book.objects.all()[0].author
'JK Rowling'
>

>>> Book.objects.all()
<QuerySet [<Book: (Lord of the Rings) (3)>, <Book: (Kinnara Thumbikal) (4)>]>
>>> Book.objects.get(id=2)
<Book: (Lord of the Rings) (3)>
>>> Book.objects.get(id=2)

 Book.objects.get(author="Shakkeela")
<Book: (Driving School) (5)>


>>> Book.objects.filter(author="Shakkeela")
<QuerySet [<Book: (Driving School) (5)>, <Book: (Kalluvaathukkal Kathreena) (3)>, <Book: (Kinnara Thumbikkal) (5)>]>
>>> 

>>> Book.objects.filter(rating__lt=4)
<QuerySet [<Book: (Lord of the Rings) (3)>, <Book: (Kalluvaathukkal Kathreena) (3)>]>


>>> Book.objects.filter(rating__lte=5)
<QuerySet [<Book: (Lord of the Rings) (3)>, <Book: (Driving School) (5)>, <Book: (Kalluvaathukkal Kathreena) (3)>, <Book: (Kinnara Thumbikkal) (5)>]>

Book.objects.filter(rating=4)
<QuerySet []>

>>> Book.objects.filter(rating__gt=4)
<QuerySet [<Book: (Driving School) (5)>, <Book: (Kinnara Thumbikkal) (5)>]>
>>> Book.objects.filter(rating__gte=4)
<QuerySet [<Book: (Driving School) (5)>, <Book: (Kinnara Thumbikkal) (5)>]>

 Book.objects.filter(author="Shakkeela",title="Kinnara Thumbikkal")
<QuerySet [<Book: (Kinnara Thumbikkal) (5)>]>
>>>

>> Book.objects.filter(author="Shakkeela",title__contains="Kinnara Thumbikkal")
<QuerySet [<Book: (Kinnara Thumbikkal) (5)>]>







>>> from book_outlet.models import Book
>>> from django.db.models import Q
>>> Book.objects.filter(Q(author="Shakkeela")|Q(title="Layanam"))
<QuerySet [<Book: (Driving School) (5)>, <Book: (Kalluvaathukkal Kathreena) (3)>, <Book: (Kinnara Thumbikkal) (5)>, <Book: (Layanam) (4)>]>
>>> 

'''