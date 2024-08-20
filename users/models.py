from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователь:
    все поля от обычного пользователя, но авторизацию заменить на email;
    телефон;
    город;
    аватарка.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=35,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Введите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )

    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    """Платежи:
    пользователь,
    дата оплаты,
    оплаченный курс или урок,
    сумма оплаты,
    способ оплаты: наличные или перевод на счет.
    """

    cash = "наличные"
    card = "перевод на счет"

    payment_method_var = [(cash, "наличные"), (card, "перевод на счет")]

    owner = models.ForeignKey(
        User, verbose_name="пользователь", on_delete=models.CASCADE
    )
    payment_date = models.DateField(verbose_name="дата оплаты")
    lesson = models.ForeignKey(
        "materials.Lesson",
        blank=True,
        null=True,
        verbose_name="оплаченный урок",
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        "materials.Course",
        blank=True,
        null=True,
        verbose_name="оплаченный курс",
        on_delete=models.CASCADE,
    )

    payment_sum = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(
        max_length=50, choices=payment_method_var, verbose_name="способ оплаты"
    )

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):
        return f"Платеж от {self.owner} на сумму {self.payment_sum}, от даты: {self.payment_date}"
