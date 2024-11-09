from rest_framework import serializers
from .models import *
class ColorSerializers(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    name=serializers.CharField(max_length=20)
    description=serializers.CharField(default="No description")

    def create(self,validated_data):
        return Color.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance
    

class ProductSerializers(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    name=serializers.CharField(max_length=40)
    price=serializers.IntegerField()
    description=serializers.CharField()
    color=ColorSerializers()

    def create(self, validated_data):
        color_data = validated_data.pop("color")  # color is now an object, but you want to use only name
        color_name = color_data.get("name")  # Extract the color name from the input data
        try:
            color = Color.objects.get(name=color_name)  # Look up the Color object using the name
            product = Product.objects.create(color=color, **validated_data)
        except Color.DoesNotExist:
            raise serializers.ValidationError({"color": f"Color {color_name} does not exist"})
        except Exception as e:
            raise serializers.ValidationError({"product": f"An error occurred while creating the product: {str(e)}"})
        return product

    def update(self, instance, validated_data):
        color_data = validated_data.pop("color", None)
        if color_data:
            color_name = color_data.get("name")  # Extract the name from the color object
            try:
                color = Color.objects.get(name=color_name)  # Look up the Color object
                instance.color = color
            except Color.DoesNotExist:
                raise serializers.ValidationError({"color": f"Color {color_name} does not exist"})
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # When returning the data, we will send the full color object as defined in ColorSerializer
        representation["color"] = instance.color.name 
        return representation