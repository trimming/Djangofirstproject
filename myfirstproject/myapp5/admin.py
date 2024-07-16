from django.contrib import admin

from .models import Category, Product
from myapp2.models import CoinFlip
from myapp4.models import Author, Article


# @admin.register(CoinFlip)
# class CoinFlipAdmin(admin.ModelAdmin):
#     list_display = ['coin_side', 'timestamp']


@admin.action(description='Сменить имя на None')
def change_name(modeladmin, request, queryset):
    queryset.update(name='None')


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'bio', 'birthday']
    ordering = ['last_name', 'birthday']
    list_filter = ['email', 'birthday']
    search_fields = ['bio']
    search_help_text = 'Поиск по полю Биография (bio)'
    actions = [change_name]
    readonly_fields = ['birthday']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Фамилия и биография автора',
                'fields': ['last_name', 'bio'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email'],

            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Дата рождения',
                'fields': ['birthday'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CoinFlip)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article)
