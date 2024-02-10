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
