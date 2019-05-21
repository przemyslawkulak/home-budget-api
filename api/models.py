from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField(default='Account', blank=True, max_length=256)
    description = models.TextField(blank=True, default='')
    account_balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, blank=True)

    def __str__(self):
        return f'Name: {self.name} Balance: {self.account_balance} {self.description}'


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    main_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='main_account')
    transfer_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transfer_account', null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.author} {self.amount}PLN {self.type} {self.category} {self.payee}'
