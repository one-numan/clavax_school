from rest_framework import serializers
from .models import Student, StudentClass


class StudentSerializers(serializers.ModelSerializer):

    """Student Entries Serializer for Class table 's Model 
    """
    class Meta:
        model = Student
        fields = '__all__'
        # exclude= ['status']
        depth = 1


class ClassSerializers(serializers.ModelSerializer):
    """Class Serializer for Class table 's Model 
    """
    # student=StudentSerializers()
    class Meta:
        model = StudentClass
        fields = '__all__'
