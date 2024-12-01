from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_link
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(validators=[validate_link])
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField(read_only=True)

    def get_lessons(self, instance):
        return [lesson.name for lesson in Lesson.objects.filter(course=instance)]

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    count_lessons_in_course = serializers.SerializerMethodField(read_only=True)

    def get_count_lessons_in_course(self, instance):
        return instance.lessons.count()
        # return Course.objects.filter(lessons=course.lesson).count()

    class Meta:
        model = Course
        fields = ("name", "description", "count_lessons_in_course", "lessons")
