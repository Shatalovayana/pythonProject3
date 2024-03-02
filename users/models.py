from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lessons

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=30, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payments(models.Model):
    PAYMENT_CASH = 'CASH'
    PAYMENT_CARD = 'CARD'
    PAYMENT_CHOICES = ((PAYMENT_CASH, 'оплата наличными'),
                       (PAYMENT_CARD, 'оплата картой')
                       )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='способ оплаты', choices=PAYMENT_CHOICES, **NULLABLE)
    payment_url = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)
    payment_id = models.CharField(max_length=255, verbose_name='id сессии оплаты', **NULLABLE)
    stripe_product_id = models.CharField(max_length=255, verbose_name='id продукта', **NULLABLE)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='оплаченный курс', **NULLABLE)
    is_signed = models.BooleanField(verbose_name='подписан ли пользователь', **NULLABLE)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user} subscribed to {self.course.name}'
