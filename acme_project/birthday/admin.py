from django.contrib import admin

from .models import Birthday, Tag


empty_value_display = 'Не задано'


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday'
    )
    list_editable = (
        'first_name',
        'last_name',
        'birthday'
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass