import datetime
from django.utils.timezone import make_aware

from apps.accounts.models import VkSession

EXPIRES_IN = 1 * 24 * 60 * 60


class AuthMixin(object):
    def auth_user(self, account):
        expires_at = make_aware(datetime.datetime.now() + datetime.timedelta(seconds=int(EXPIRES_IN)))
        vk_session = VkSession.objects.create(account=account, access_token='test_token', expires_at=expires_at)

        session = self.client.session
        session['vk_session_id'] = vk_session.id
        session['access_token'] = 'test_token'
        session['account_id'] = account.id
        session['vk_id'] = account.vk_id
        session.save()
