from datetime import timedelta
from celery import shared_task
from django.conf import settings
from django.utils import timezone

from .models import Account

@shared_task
def delete_unverified_accounts():
    """
    Celery task to delete inactive accounts that have not verified their email within 24 hours.
    """
    retention_period = timedelta(hours=
                                 getattr(settings, 'INACTIVE_ACCOUNT_EXPIRATION_HOURS', 24)
                                 )
    expiration_time = timezone.now() - retention_period
    unverified_accounts, _ = Account.objects.filter(email_verified=False,date_joined__isnull=False, date_joined__lt=expiration_time).delete()


    return{
        "deleted_accounts": unverified_accounts,
        "expiration_time": expiration_time.isoformat(),
    }


@shared_task
def delete_expired_disabled_accounts():
    """
    Celery task to delete accounts that have been disabled for more than 30 days.
    """
    retention_period = timedelta(days=
                                 getattr(settings, 'DISABLED_ACCOUNT_RETENTION_DAYS', 30)
                                 )
    expiration_time = timezone.now() - retention_period
    deleted_count, _ = Account.objects.filter(is_active=False,disabled_at__isnull=False, disabled_at__lte=expiration_time).delete()

    return {
        "deleted_accounts": deleted_count,
        "expiration_time": expiration_time.isoformat(),
    }