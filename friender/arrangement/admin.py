from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.db.models import F
from django.utils.safestring import mark_safe


class UserRatingInLine(admin.StackedInline):
    model = UserRating
    extra = 2

class HobbiesInLine(admin.TabularInline):
    model = Hobbies.user.through
    extra = 0


@admin.action(description='Change city')
def change_city(modeladmin, request, queryset):
    queryset.update(city='Baranovichi')

# @admin.action(description='year_later')
# def year_later(modeladmin, request, queryset):
#     queryset.update(age = F('age'+1)
#


# @admin.display(description='Name')
# def upper_case_name(obj):
#     return ("%s %s" % (obj.name, obj.surname)).upper()


@admin.display(description='Столица')
def check_capital(object):
    return 'capital' if object.city in ['Minsk','Moscow'] else 'simple city'

color_code  = 'FF33E0'

@admin.display(description='фото')
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):

    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            color_code,
            self.name,
            self.surname,
        )


    fields = ['name','surname','age','sex','email','city', 'photo'] #вывод поле внутри ячейки
    list_display = (colored_name,'age','sex','email',get_html_photo, 'city',check_capital) #колонки
    list_display_links = [colored_name] #активные поля
    list_editable = ['age', 'city'] #поля, которые можно сразу менять
    ordering = ['name'] #сортировка по имени
    search_fields = ['sex','city','age'] #поиск по значению
    list_per_page = 10  #количесво записей на странице
    list_filter = ['age','sex','city'] # сортировка по выбранным даным (можно сразу все поля выбирать)
    save_on_top = True
    inlines = [
        UserRatingInLine,
        HobbiesInLine

    ]
    actions = [change_city]


@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):

    list_display = ["rating", "user", get_html_photo]
    list_display_links = ['rating', 'user']



# class HostAdmin(admin.ModelAdmin):
#     pass
# class GuestAdmin(admin.ModelAdmin):
#     pass
#
class HobbiesAdmin(admin.ModelAdmin):
    fields = ['hobby','category','user']
    list_display = ['hobby','category']
    list_display_links = ['hobby', 'category']
    search_fields = ['hobby']
    ordering = ['hobby']
    filter_horizontal = ('user',)
    inlines = [
        HobbiesInLine
    ]
class PassportAdmin(admin.ModelAdmin):
    fields = ['passport_id','user']
    list_display = ['passport_id','user']
    list_display_links = ['passport_id','user']
@admin.register(Establishments)
class EstablishmentsAdmin(admin.ModelAdmin):

    # get_html_photo.short_descriptions = 'фото'

    fields = ['name','category','address','phone','photo']
    list_display = ['name','category',get_html_photo]
    list_display_links = ['name','category']
    search_fields = ['name', 'category']

class RatingAdmin(admin.ModelAdmin):
    fields = ['rating', 'description']
    list_display = ['establishment', 'rating', 'description']



# @admin.display
# def colored_name(self):
#     return format_html(
#         '<span style="color: #{};">{} {}</span>',
#         color_code,
#         self.name,
#         self.surname,
#     )
#
# admin.site.register(Users, UsersAdmin)
# admin.site.register(UserRating)
admin.site.register(Hobbies, HobbiesAdmin)
admin.site.register(EstablishmentsRating, RatingAdmin)
# admin.site.register(Establishments, EstablishmentsAdmin)
admin.site.register(Passport, PassportAdmin)
admin.site.register(Arrangements)
admin.site.register(Host)
admin.site.register(Guest)

# Register your models here.
