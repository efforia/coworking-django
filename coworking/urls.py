from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic.base import TemplateView

from filebrowser.sites import site

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns("",
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += [
    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the index.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),

    # STATIC TEMPLATE PAGES

    url(r'^coworking/', TemplateView.as_view(template_name="coworking.html"), name="coworking"),
    url(r'^fotos/', TemplateView.as_view(template_name="photos.html"), name="photos"),
    url(r'^planos/', TemplateView.as_view(template_name="pricing.html"), name="pricing"),
    url(r'^servicos/', TemplateView.as_view(template_name="services.html"), name="services"),
    url(r'^agenda/', TemplateView.as_view(template_name="agenda.html"), name="agenda"),
    url(r'^sobre/', TemplateView.as_view(template_name="about.html"), name="about"),
]
