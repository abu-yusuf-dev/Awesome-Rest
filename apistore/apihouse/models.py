from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    full_name = models.CharField(max_length=500)
    email = models.EmailField()
    civil_no = models.PositiveIntegerField()
    state = models.CharField(max_length=500)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return self.full_name

