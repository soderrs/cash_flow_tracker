from django.contrib import admin
from django import forms

import core


@admin.register(core.models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [
        core.models.Subcategory.name.field.name,
        core.models.Subcategory.category.field.name,
    ]


@admin.register(core.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        core.models.Category.name.field.name,
        core.models.Category.type.field.name,
    ]


@admin.register(core.models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = [core.models.Type.name.field.name]


@admin.register(core.models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [core.models.Status.name.field.name]


@admin.register(core.models.Entry)
class EntryAdmin(admin.ModelAdmin):
    class Media:
        js = [
            "js/admin.js",
        ]

    list_display = [
        core.models.Entry.date.field.name,
        core.models.Entry.status.field.name,
        core.models.Entry.type.field.name,
        core.models.Entry.category.field.name,
        core.models.Entry.subcategory.field.name,
        core.models.Entry.amount.field.name,
        core.models.Entry.comment.field.name,
    ]
    list_filter = [
        core.models.Entry.date.field.name,
        core.models.Entry.status.field.name,
        core.models.Entry.type.field.name,
        core.models.Entry.category.field.name,
        core.models.Entry.subcategory.field.name,
    ]
