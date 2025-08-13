from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'
        #fields = ['id', 'name', 'description']
        #exclude = ['active']

    def get_len_names(self, object):
        return len(object.name)
    

    def validate_name(self, value): #Field Level Validation, checking a particular field
        if len(value) < 2:
            raise serializers.ValidationError('Name should be at least 2 characters long.')
        else:
            return value
        
    def validate(self, data): #Object Level Validation, checking the whole object
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description cannot be the same.')
        return data



# def name_length(value): #Validators, instead of field level validation
#         if len(value) < 2:
#             raise serializers.ValidationError('Name should be at least 2 characters long.')
#         else:
#             return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name =validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # def validate_name(self, value): #Field Level Validation, checking a particular field
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError('Name should be at least 2 characters long.')
#     #     else:
#     #         return value
        
#     def validate(self, data): #Object Level Validation, checking the whole object
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description cannot be the same.')
#         return data
