from rest_framework import serializers
from watchlist_app.models import Movie

# validators
def name_check(value):
    if len(value) < 2:
        raise serializers.ValidationError("Title length is too short")

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_check])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        
        return instance
    
    # field validator
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Title length is too short")
    #     else:
    #         return value
        

    #object validator
    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Title and description cannot be the same")
        else:
            return data
    