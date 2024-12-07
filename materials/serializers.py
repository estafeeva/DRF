from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
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
    is_user_subscript = serializers.SerializerMethodField(read_only=True)

    def get_count_lessons_in_course(self, instance):
        return instance.lessons.count()
        # return Course.objects.filter(lessons=course.lesson).count()

    def get_is_user_subscript(self, instance):
        """
        Информация, подписан пользователь на обновления курса или нет.
        """
        a = Subscription.objects.filter(course=instance).filter(
            user=self.context["request"].user
        )
        return a.exists()

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "count_lessons_in_course",
            "lessons",
            "is_user_subscript",
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
