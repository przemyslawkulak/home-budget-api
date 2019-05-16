from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField(default='Account', blank=True, max_length=256)
    description = models.TextField(blank=True)
    account_balance = models.IntegerField(default=0)

    def __str__(self):
        return f'Name: {self.name} Balance: {self.account_balance}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} '


class Payee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} '


TYPE = (
    (0, 'Withdrawal'),
    (1, 'Deposit'),
    (2, 'Transfer'),
)


class Transaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    type = models.IntegerField(choices=TYPE)
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE, related_name='payee', null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='category')
    description = models.TextField(blank=True, null=True)
    amount = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.author} {self.amount}PLN {self.type} {self.category} {self.payee}'
