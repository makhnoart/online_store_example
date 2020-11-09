from rest_framework import serializers
from apps.member.models import User, UserEmailConfirm
from rest_framework.authtoken.models import Token


class UserSignUpSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email already exists!')
        return value

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError('Passwords not the same!')
        return attrs

    def create(self, validated_data):
        validated_data['password'] = validated_data.pop('password1')
        del validated_data['password2']
        user = User.objects.create_user(
            email=validated_data['email'],
            is_active=False,
            **validated_data
        )
        email_confirm = UserEmailConfirm.objects.create(user=user)
        email_confirm.send()
        return user


class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    auth_token = serializers.CharField(source='key', read_only=True)

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            user = None
        if user is None or not user.check_password(attrs['password']):
            raise serializers.ValidationError('Incorrect credentials!')
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        token = Token.objects.create(user=user)
        return token


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()


class SuperUserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()


class UserEmailConfirmSerializer(serializers.Serializer):
    key = serializers.UUIDField()

    def validate(self, attrs):
        try:
            email_confirm = UserEmailConfirm.objects.get(key=attrs['key'])
        except UserEmailConfirm.DoesNotExist:
            email_confirm = None
        if email_confirm is None or email_confirm.is_valid == False:
            raise serializers.ValidationError('Invalid key!')
        user = email_confirm.user
        if user.is_active:
            raise serializers.ValidationError('User already active!')
        attrs['user'] = user
        return attrs

    def create(self, validated_data):

        user = validated_data.pop('user')
        user.is_active = True
        user.save()
        return validated_data

