from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Account, Category, Payee, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payee
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'username', 'date_joined')
