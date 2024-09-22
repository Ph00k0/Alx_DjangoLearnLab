from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }word": "Password fields didn't match."})
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        })
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }
# Override the create method to handle custom user creation
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Create the user using the User model's create_user method
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # Set the password properly
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        # Check if user already has a token, if not, create one
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in the response
        return {
            "user": user,
            "token": token.key
        }write_only=True)
