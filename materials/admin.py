from django.contrib import admin

from materials.models import Course, Lesson, Subscription


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "owner")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("course", "user")
