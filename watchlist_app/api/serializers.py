from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform




class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    #nested serializer (connecting to many watchlist in one platform)
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:

        model = StreamPlatform
        fields = "__all__"




# Model Serializers
# class MovieSerializer(serializers.ModelSerializer):

#     #custom field addition
#     name_len = serializers.SerializerMethodField()

#     class Meta:

#         model = Movie
#         fields = "__all__"  # this with include all the fields
#         # fields = ["id", "name"] # include only the fileds that we mention here
#         # exclude = ["id"] # fields that we want to exclude

    
#     #custom field addition inside serializer
#     def get_name_len(self, object):
#         return len(object.name)


    
#     # field validator
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Title length is too short")
#         else:
#             return value
        

#     #object validator
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and description cannot be the same")
#         else:
#             return data



# validators
# def name_check(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Title length is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_check])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
        
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
        
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
        
#         return instance
    
#     # field validator
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Title length is too short")
#     #     else:
#     #         return value
        

#     #object validator
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and description cannot be the same")
#         else:
#             return data
    