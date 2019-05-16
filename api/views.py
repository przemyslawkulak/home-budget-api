from django.contrib.auth.models import User
from rest_framework import viewsets

from api.models import Account, Category, Payee, Transaction
from api.serializers import AccountSerializer, CategorySerializer, PayeeSerializer, TransactionSerializer, \
    UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PayeeViewSet(viewsets.ModelViewSet):
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
