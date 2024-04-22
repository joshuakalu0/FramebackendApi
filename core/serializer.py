from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['pk','username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(validated_data)


class MyTokenObtainPair(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        '''
        fill token with desired values
        '''
        token = super().get_token(user)
        # token['gender'] = user.gender
        return token