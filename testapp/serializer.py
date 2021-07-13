from rest_framework import serializers
from .models import Hotel,Student

class MoviesSerializer(serializers.ModelSerializer):
    file=serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = Hotel
        #fields = '__all__'
        fields=('id','name','file')

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.password=validated_data.get('password',instance.password)
        instance.marks=validated_data.get('marks',instance.marks)
        instance.save()
        return instance