from django.contrib import admin
from django.contrib.auth.models import User

from api.models import Account, Category, Payee, Transaction

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Payee)
admin.site.register(Transaction)
admin.site.register(User)
