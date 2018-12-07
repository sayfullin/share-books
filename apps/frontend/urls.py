from django.conf.urls import url
from django.views.generic import TemplateView

from apps.frontend.views import AppView, VkRedirectUrl


urlpatterns = [
    url(r'^app/$', AppView.as_view(), name='app'),
    url(r'^vk_redirect_uri/$', VkRedirectUrl.as_view(), name='vk-redirect-uri'),
    url(r'^$', TemplateView.as_view(template_name='frontend/login_form.html'), name='login-form'),
]