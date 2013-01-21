from django.contrib.sitemaps import Sitemap
from garitas.models import MexCity


class GaritasSitemap(Sitemap):
    changefreq = "Monthly"
    priority = 0.8

    def items(self):
        return MexCity.objects.all()
