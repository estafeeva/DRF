from django.db import models

from users.models import User


class Course(models.Model):
    """Курс:
    название,
    превью (картинка),
    описание."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="Описание курса",
        help_text="Введите описание курса",
    )
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name"]


class Lesson(models.Model):
    """Урок:
    название,
    описание,
    превью (картинка),
    ссылка на видео."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )
    preview = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        max_length=100,
        verbose_name="Курс",
        help_text="Введите курс, в который входит урок",
        null=True,
        blank=True,
        related_name="lessons",
    )

    video_link = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        verbose_name="CСсылка на видео урока",
        help_text="Добавьте ссылку на видео урока",
    )

    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


"""        permissions = [
            ("set_published", "Can publish posts"),
            ("change_description", "Can change description"),
            ("change_category", "Can change category"),
        ]
"""

"""Урок и курс - это связанные между собой сущности.
Уроки складываются в курс, в одном курсе может быть много уроков."""
