from rest_framework import serializers
from .models import User

#En el paréntesis le estoy diciendo que desde serializers voy a crear un Model serializer
class UserSerializerRead(serializers.Serializer):
    id=serializers.IntegerField()
    username=serializers.CharField(max_length=20,help_text="El nombre debe ser único")
    full_name=serializers.CharField()
   
class UserSerializerWrite(serializers.Serializer):
    username=serializers.CharField(max_length=20, help_text="El nombre debe ser único")
    first_name=serializers.CharField(max_length=20)
    last_name=serializers.CharField(max_length=20,allow_null=True,required=False,allow_blank=True)
    password=serializers.CharField(max_length=20)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
        
class UserSerializer3(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","password"]