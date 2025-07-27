from django.contrib import admin
from home.models import Home, Job


class HomeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")
    search_fields = ("name",)


class JobAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Home, HomeAdmin)
admin.site.register(Job, JobAdmin)
