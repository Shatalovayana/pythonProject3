from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lessons
from materials.paginators import MaterialsPaginator
from materials.permissions import IsModerator, IsCourseOwner, IsStaff, \
    IsLessonsOwner
from materials.serializers import CourseSerializer, LessonsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPaginator

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsModerator | IsCourseOwner | IsStaff, IsAuthenticated]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsCourseOwner | IsStaff]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPaginator


class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated]


class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonsOwner | IsStaff]


class LessonsDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
    permission_classes = [IsAuthenticated, IsLessonsOwner | IsStaff]
