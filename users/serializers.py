from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# refer to custom user model with settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    school = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'],
                                        validated_data['school'])
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'school', 'password')
