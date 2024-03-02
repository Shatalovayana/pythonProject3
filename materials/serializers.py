from rest_framework import serializers

from materials.models import Course, Lessons
from materials.validators import LinkValidator


class LessonsSerializer(serializers.ModelSerializer):
    link = serializers.URLField(max_length=150,
                                validators=[LinkValidator(field='link')]
                                )

    class Meta:
        model = Lessons
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(source='lessons_set', many=True, read_only=True)
    is_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lessons_set.all().count()

    def get_is_subscribe(self, instance):
        return instance.subscription_set.filter(user=self.context['request'].user).exists()

