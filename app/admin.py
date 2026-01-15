from django.contrib import admin
from django.utils.html import format_html
from .models import BannerImage, AboutUs, Service


# ===================== BANNER IMAGE ADMIN =====================
@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    readonly_fields = ("image_preview",)
    list_per_page = 10

    fieldsets = (
        ("Banner Image", {
            "fields": ("image", "image_preview"),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:120px;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


# ===================== ABOUT US ADMIN =====================
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    readonly_fields = ("image_preview",)
    list_per_page = 10

    fieldsets = (
        ("About Us Image", {
            "fields": ("image", "image_preview"),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:120px;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


# ===================== SERVICE ADMIN =====================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image_preview")
    search_fields = ("title", "description")
    list_filter = ("title",)
    readonly_fields = ("image_preview",)
    list_per_page = 15
    ordering = ("title",)

    fieldsets = (
        ("Service Information", {
            "fields": ("title", "description"),
        }),
        ("Service Image", {
            "fields": ("image", "image_preview"),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:100px;border-radius:8px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"
