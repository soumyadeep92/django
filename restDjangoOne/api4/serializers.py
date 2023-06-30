from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields=['name','roll','city']
        # read_only_fields=['name','roll']
        extra_kwargs={'name':{'read_only':True}}

# def starts_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should start with r')

# class StudentSerializer(serializers.Serializer):
    # name=serializers.CharField(max_length=100,validators=[starts_with_r])
    # roll=serializers.IntegerField()
    # city=serializers.CharField(max_length=100)
    # def create(self,validated_data):
    #     return Student.objects.create(**validated_data)
    # def update(self,instance,validated_data):
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.roll=validated_data.get('roll',instance.roll)
    #     instance.city=validated_data.get('city',instance.city)
    #     instance.save()
    #     return instance
    # def validate_roll(self,value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat full')
    #     return value
    # def validate(self,data):
    #     name=data.get('name')
    #     city=data.get('city')
    #     if name.lower() == 'rohit' and city.lower() != 'Ranchi':
    #         raise serializers.ValidationError('City should be Ranchi')
    #     return data