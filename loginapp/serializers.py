from rest_framework import serializers
from .models import logininfo
from django.contrib.auth.hashers import make_password

class loginfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=logininfo
        fields =['username','password']

    



