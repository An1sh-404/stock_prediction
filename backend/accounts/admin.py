from django.contrib import admin
from django.utils import timezone
from .models import Account

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff', 'email_verified', 'disabled_at')
    list_filter = ('is_active', 'is_staff', 'email_verified')
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined',)


    def save_model(self, request, obj, form, change):
        was_active = True

        if change:
            # Fetch the original object from the database to check its previous state
            previous = Account.objects.get(pk=obj.pk)
            was_active = previous.is_active

        if was_active and not obj.is_active:
            obj.disabled_at = timezone.now()

        elif not was_active and obj.is_active:
            obj.disabled_at = None

        super().save_model(request, obj, form, change)