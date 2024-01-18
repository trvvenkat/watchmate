from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            'password': {"write_only": True}
        }
        
    def save(self):
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        
        if password2 != password:
            raise serializers.ValidationError("Passwords do not match")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        
        account = User.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        
        return account
        
        
        