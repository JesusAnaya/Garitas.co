#-*- coding: utf-8 -*-
from django.contrib import admin
from garitas.models import MexCity, Border


class MexCityAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'state', 'link', 'go_to_link')

    def go_to_link(self, obj):
        return "<a href='/%s' target='_blank'>%s</a>" % (obj.link, obj.link)
    go_to_link.allow_tags = True


class BorderAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'border_id', 'latitude', 'longitude')


admin.site.register(MexCity, MexCityAdmin)
admin.site.register(Border, BorderAdmin)
