from django.db import models
from django.contrib.auth.models import AbstractUser, User


# list_of_categories = ((0, 'inne'),
#                       (1, 'odzież'),
#                       (2, 'motoryzacja'),
#                       (3, 'usługi'),
#                       (4, 'żywność'),
#                       (5, 'sport'),
#                       (6, 'nauka'),)

class TableUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_details = models.TextField()

    def __str__(self):
        return f'{self.user.username}, {self.contact_details}'


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(null=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(TableUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.title