from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lessons
from materials.permissions import IsModerator, IsOwnerOrStaff
from materials.serializers import CourseSerializer, LessonsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            self.permission_classes = [IsModerator | IsOwnerOrStaff, IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsModerator | IsOwnerOrStaff]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsOwnerOrStaff, IsModerator]


class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated]


class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsModerator, IsOwnerOrStaff]


class LessonsDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
    permission_classes = [IsOwnerOrStaff]
