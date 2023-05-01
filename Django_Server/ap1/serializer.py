from rest_framework import serializers
# from .models1 import User_Details,SignUp
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
User = get_user_model() 

class UserdetailSeriazlier(serializers.ModelSerializer):
    # username= serializers.SerializerMethodField("get_username")
    class Meta:
        model= User
        fields= ['username','email','mobile_num']
    # def get_username(self,obj1):
    #     # print(obj1)
        
    #     # return obj1
    
        
    
class UserSeriazlier(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username','password','mobile_num','email']
        extra_kwargs = {"password":{'write_only': True}}
    def validate(self, attrs):
        print(attrs)
        email=attrs.get('email','')
        mobile_num=attrs.get('mobile_num','')
        username=attrs.get('username','')
        # if len(username) > 20:
        #     raise serializers.ValidationError("Length of Username must be less then 20")
            
        password=attrs.get('password','')
        
        # if len(mobile_num) > 10 or len(mobile_num) < 10:
        #     raise serializers.ValidationError("Length of Mobile must be 10")
        # if not mobile_num.isnumeric() :
        #     raise serializers.ValidationError("The Mobile must be numberic")
        return attrs
    def create(self, validated_data): 
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return validated_data
        
class SignupSeriazlier(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
        
