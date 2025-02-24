from rest_framework import viewsets
from rest_framework import permissions

from student.models import StudentModel

from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = StudentModel.objects.all()
    # 指定序列化的类
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]