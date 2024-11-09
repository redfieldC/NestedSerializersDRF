from rest_framework import serializers
from .models import *
class ColorSerializers(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    name=serializers.CharField(max_length=20)
    description=serializers.CharField()

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
    color=serializers.CharField(source="color.name")

    def create(self, validated_data):
        color_name = validated_data.pop("color")["name"]
        try:
            color = Color.objects.get(name=color_name)
            product = Product.objects.create(color=color, **validated_data)
        except Color.DoesNotExist:
            raise serializers.ValidationError({"color": f"Color {color_name} does not exist"})
        except Exception as e:
            raise serializers.ValidationError({"product": f"An error occurred while creating the product: {str(e)}"})

        

        return product
    
    def update(self,instance,validated_data):
        color_name=validated_data.pop("color",None)
        if color_name:
            try:
                color=Color.objects.get(name=color_name["name"])
                instance.color=color 
            except Color.DoesNotExist:
                raise serializers.ValidationError({"color":f"Color {color_name['name']} does not exist"})
        
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance
