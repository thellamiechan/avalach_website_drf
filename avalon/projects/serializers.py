from rest_framework import serializers
from django.apps import apps

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('projects.Project')
        fields ='__all__'

class ProjectDetailSerializer(ProjectSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance