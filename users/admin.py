from django.contrib import admin

from users.models import User, Payments, Subscription

admin.site.register(User)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'date_of_payment', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method',)
    search_fields = ('paid_course', 'paid_lesson',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course', 'is_signed',)
    search_fields = ('course',)
