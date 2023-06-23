from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model





class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(required=True)
  


    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username Already Exixts")
        return data
    

    def create(self, validated_data):
        user = get_user_model.create_user(**validated_data)
        #user = User.objects.create(first_name=validated_data['first_name'],
        #last_name= validated_data['last_name'],username =validated_data['username'].lower())
        #user.set_password(validated_data['password'])
        #validated_data.pop('password')

        return validated_data
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):

        if not User.objects.filter(username=data['username']):
            raise serializers.ValidationError("User Does Not Exist")
        return data
    
    def jwt_token(self,data):

        user = authenticate(username=data['username'],password=data['password'])

        if not user:
            return {"error":"Invalid Credentials","data":{}}
        
        refresh = RefreshToken.for_user(user)

        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "message":"Login SucessFul"
        }


