from allauth.account.signals import user_logged_in, user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver


def sync_google_data(user, extra_data):
    if not extra_data:
        return

    print("GOOGLE DATA:", extra_data)

    first = extra_data.get("given_name")
    last = extra_data.get("family_name")

    if first:
        user.first_name = first

    if last:
        user.last_name = last

    if not last and extra_data.get("name"):
        full_name = extra_data.get("name").split()
        if len(full_name) > 1:
            user.last_name = full_name[-1]

    if not user.username:
        user.username = extra_data.get("email").split("@")[0]

    user.save(update_fields=["first_name", "last_name", "username"])


@receiver(user_signed_up)
def google_signup(request, user, sociallogin=None, **kwargs):
    if sociallogin and sociallogin.account.provider == "google":
        sync_google_data(user, sociallogin.account.extra_data)


@receiver(user_logged_in)
def google_login(request, user, **kwargs):
    try:
        social = SocialAccount.objects.get(user=user, provider="google")
        sync_google_data(user, social.extra_data)
    except SocialAccount.DoesNotExist:
        pass
