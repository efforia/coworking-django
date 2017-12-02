from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
# from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

# urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    # url("^admin/", include(admin.site.urls)),
# )

urlpatterns = [
    url("^admin/", include(admin.site.urls)),
    url("^$", TemplateView.as_view(template_name="index.html"), name="home"),

    # STATIC TEMPLATE PAGES

    url(r'^coworking/', TemplateView.as_view(template_name="coworking.html"), name="coworking"),
    url(r'^fotos/', TemplateView.as_view(template_name="photos.html"), name="photos"),
    url(r'^planos/', TemplateView.as_view(template_name="pricing.html"), name="pricing"),
    url(r'^servicos/', TemplateView.as_view(template_name="services.html"), name="services"),
    url(r'^mentoria/', TemplateView.as_view(template_name="services.html"), name="services"),
    url(r'^agenda/', TemplateView.as_view(template_name="agenda.html"), name="agenda"),
    url(r'^sobre/', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^parceiros/', TemplateView.as_view(template_name="partners.html"), name="partners"),

]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
urlpatterns += staticfiles_urlpatterns()
