from rest_framework import serializers
from .models import CustomUser,Package,Comments,Blogs,Review
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {'Custom message':' No active account found with the given credentials'},
        'blank_username': 'Custom message: Please fill in all required fields.',
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # adding custom claims
        token['current_user'] = user.username
        token['is_superuser'] = user.is_superuser
        print(token)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.is_superuser==False:
            data["is_superuser"] = user.is_superuser
            data["current_user"] = user.username
    
            return data
        else:
            raise serializers.ValidationError("Only commom users are allowed to log in here.")
        
   
        
    
class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # adding custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.is_superuser==True:
                data["is_superuser"] = user.is_superuser
                data["username"] = user.username
                return data
        else:
            raise serializers.ValidationError(" Only administrators are allowed to log in here.")



class CustomUserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone', 'place', 'image', 'password','password_confirmation')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        try:
            CustomUser.objects.get(email=data['email'])
            raise serializers.ValidationError({'email':'Email already exists.'})
        except ObjectDoesNotExist:
            pass

        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({'password_confirmation':"Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CustomUserupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','image','phone','place','email']
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email__iexact=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value
    

class PackageSerializer(serializers.ModelSerializer):
    #hotel=serializers.ImageField(max_length=None,use_url=True,required=False)
    class Meta:
        model = Package
        exclude = ['admin']

class PackagelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment']

class CommentlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        exclude = ['user']

class BloglistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['user']
        
class ReviewlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

# class TranslationSerializer(serializers.Serializer):
#     original_content = serializers.CharField(max_length=1000)
#     target_language = serializers.CharField(max_length=10, default='en')


from rest_framework import serializers

class TranslateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    target_language = serializers.CharField(default='en')
    
    # class Meta:
    #     fields = ['text', 'target_language']

    # def validate_target_language(self, value):
    #     allowed_languages = ['en', 'fr', 'es']  # Allowed languages: English, French, Spanish
    #     if value.lower() not in allowed_languages:
    #         raise serializers.ValidationError(f"Target language must be one of {', '.join(allowed_languages)}")
    #     return value.lower()