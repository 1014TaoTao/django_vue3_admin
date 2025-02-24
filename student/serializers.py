from rest_framework import serializers

from .models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel  # 指定的模型类
        fields = '__all__'  # 需要序列化的属性
