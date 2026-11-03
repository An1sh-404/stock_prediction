import re
import unicodedata

from django.db import transaction, IntegrityError
from django.utils import timezone
from .models import Account

def build_unique_username(seed: str) -> str:
    """
    Generates a unique username based on the provided seed string.
    The username is normalized, lowercased, and stripped of non-alphanumeric characters.
    If the generated username already exists, a numeric suffix is added to ensure uniqueness.
    """
    # Normalize and lowercase the seed
    normalized_seed = (unicodedata.normalize('NFKD', seed).encode('ascii', 'ignore').decode('ascii').lower())
    base = re.sub(r'[^a-z0-9_]', '_', normalized_seed)
    base = base.strip('_')
    base = base[:15]  # Limit to 15 characters

    if not base:
        base = 'user'

    if len(base) < 4:
        base = f'{base}_user'

    candidate = base

    # Check for existing usernames and append a numeric suffix if necessary
    suffix = 1
    while Account.objects.filter(username=candidate).exists():
        suffix_text = str(suffix)
        available_length = 15 - len(suffix_text)
        candidate = f"{base[:available_length]}{suffix_text}"
        suffix += 1

    return candidate


@transaction.atomic
def get_or_create_google_account(email: str, google_sub: str, display_name: str = '', ) -> tuple[Account, bool]:
    """
    Retrieves an existing account by email or creates a new one for Google users.
    If the account exists, it returns the account and False.
    If the account does not exist, it creates a new account with the provided email, google_sub, and display_name,
    and returns the new account and True.
    """

    email = email.strip().lower()
    google_sub = google_sub.strip()
    existing_account = (Account.objects.select_for_update().filter(google_sub=google_sub).first())

    if existing_account is not None:
        return existing_account, False

    existing_email_account = (
        Account.objects.select_for_update().filter(email=email).first()
    )

    if existing_email_account is not None:
        raise ValueError(
            'This email is associated with an existing account. Sign in using your existing method to link your Google account.'
        )


    email_seed = email.split('@',1)[0]
    username_seed = display_name.strip() or email_seed

    for _ in range(3):
        username = build_unique_username(username_seed)
        try:
            with transaction.atomic(): # An Inner SAVEPOINT for database rollback in case of race conditions
                account = Account.objects.create_google_user(
                    email=email,
                    username=username,
                    google_sub=google_sub,
                )
        except IntegrityError:
            existing_google_account = Account.objects.filter(
                google_sub=google_sub
            ).first()

            if existing_google_account is not None:
                return existing_google_account, False

            existing_email_account = Account.objects.filter(email=email).first()

            if existing_email_account is not None:
                raise ValueError(
                    "This email is associated with an existing account." \
                    "Sign in using your existing method to link your Google account."
                ) from None

            continue

        return account, True

    raise ValueError(
        "Unable to create the Google account. Please try again."
    )




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
