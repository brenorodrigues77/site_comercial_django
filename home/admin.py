from django.contrib import admin
from django.utils.html import format_html
from home.models import Home, Job


class HomeAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))
        return "-"

    image_tag.short_description = "Imagem"

    list_display = ("name", "description", "image_tag", )
    search_fields = ("name",)


class JobAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Home, HomeAdmin)
admin.site.register(Job, JobAdmin)
