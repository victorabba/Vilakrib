from rest_framework import serializers
from .models import User
from vilaproj import settings
from django.db.models.fields import Field
from allauth.account.adapter import get_adapter
from vialpi.models import ContactUs



class RegisterSerializer(serializers.Serializer):
     Register_as=serializers.CharField(max_length=200)
     first_name = serializers.CharField( write_only=True)
     last_name = serializers.CharField(write_only=True)
     email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
     username=serializers.CharField(max_length=30)
     phone_number=serializers.CharField(max_length=300)
     password=serializers.CharField(required=True, write_only=True)
     #password2=serializers.CharField(required=True, write_only=True)

     class Meta:
         model=User
         fields=('Register_as','first_name','last_name','email','username','phone_number','password')
    
     #def validate_password1(self, password):
        #return get_adapter().clean_password(password)

     #def validate(self, data):
        #if data['password1'] != data['password2']:
           # raise serializers.ValidationError(
                #("The two password fields didn't match."))
        #return data

     def create(self,validated_data):
       # del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        return user


     def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        phone_number=args.get('phone_number', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number': ('phone_number already exists')})
        return super().validate(args)

        
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields=('id','full_name','email','phone_number','your_message')


