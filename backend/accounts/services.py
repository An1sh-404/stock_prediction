from django.db import transaction
from django.utils import timezone
from .models import Account

@transaction.atomic
def disable_account(account: Account) -> Account:
    """
    Disables the given account by setting is_active to False and recording the disabled_at timestamp.
    """
    if account.is_active:
        account.is_active = False
        account.disabled_at = timezone.now()
        account.save(update_fields=['is_active', 'disabled_at'])

    return account


@transaction.atomic
def enable_account(account: Account) -> Account:
    if not account.is_active or account.disabled_at is not None:
        account.is_active = True
        account.disabled_at = None
        account.save(update_fields=['is_active', 'disabled_at'])


    return account
