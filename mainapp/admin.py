from django.contrib import admin

from mainapp.models import District, Category, CompanyGroup, Product, Company, Price


admin.site.register(District)
admin.site.register(Category)
admin.site.register(CompanyGroup)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_group', 'get_districts')

    def get_districts(self, obj):
        return ', '.join([d.name for d in obj.districts.all()])

    get_districts.short_description = 'Районы'


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'company', 'price')
